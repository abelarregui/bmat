import csv
import pandas as pd
import numpy as np
from .aux_functions import clean_string_iswc


class CsvSourceType:

    def __init__(self, path_file):
        """
        Class for manipulating csv musical works files of Type1:
            - csv file, comma separated.
            - Columns: ['ISWC', 'ORIGINAL TITLE', 'ALTERNATIVE TITLE 1', ' ALTERNATIVE TITLE 2',
                       'ALTERNATIVE TITLE 3', 'RIGHT OWNER', 'ROLE', 'IPI NUMBER',
                       'ID SOCIETY']

        :param path_file: absolute path of the file to read.
        """
        self.path_file = path_file
        unique_ids = set()
        # Create generator to read csv
        data_gen_tmp = self.__create_generator()
        # Read csv for extracting unique ids (needed for finding all rows for the same musical work)
        for row in data_gen_tmp:
            # print(row[8])
            unique_ids.add(row[8])
        # All unique ids are stored in memory. For avoiding this, a new txt file could be created
        self.unique_id_society = unique_ids

    def __create_generator(self):
        with open(self.path_file, "r", encoding='latin1') as csv_file:
            data_reader = csv.reader(csv_file)
            self.columns = next(data_reader)
            for row in data_reader:
                yield row  # yield the header row


    def generator(self, id_society=None):
        with open(self.path_file, "r", encoding='latin1') as csv_file:
            data_reader = csv.reader(csv_file)
            for row in data_reader:
                if row[8] == id_society:
                    yield row  # yield the header row

    def parsed_data(self):
        """
        Transform csv file to a list of dictionaries, according the specification.
        :return: list_works (list of dictionaries)
        """
        for id_society in self.unique_id_society:
            print(id_society)
            data_gen = self.generator(id_society)
            df = pd.DataFrame()
            for row in data_gen:
                # print(row)
                df = df.append([row], ignore_index=True)
            df.columns = self.columns
            d = {}
            df = df.reset_index(drop=True)

            # Parse _id. Same value for all the work's tuples is assumed
            d['_id'] = int(df['ID SOCIETY'].loc[0])
            # Parse ISWC. Same value for all the work's tuples is assumed
            d['iswc'] = clean_string_iswc(df['ISWC'].loc[0])

            # Parse titles
            d['titles'] = []
            # OriginalTitle: a loop has been used because possible different Original Titles.
            for title in df['ORIGINAL TITLE'].unique():
                d['titles'].append({'title': title, "type": 'OriginalTitle'})

            # AlternativeTitles: All unique values are calculated.
            # Then, new dictionaries are added to the list
            alt_titles = pd.unique(df.filter(regex='ALTERNATIVE TITLE').values.ravel())
            alt_titles = alt_titles[~pd.isnull(alt_titles)]
            for alt_title in np.unique(alt_titles):
                if alt_title != '':
                    d['titles'].append({'title': alt_title, "type": 'AlternativeTitle'})

            # Parse Right Owners data_sources
            # All rows will be read in order to parse all composers/authors, even with the same name.
            # IPI is not used due to lack of data_sources in some tuples
            d['right_owners'] = []
            for index, row in df.iterrows():
                name = row['RIGHT OWNER']
                role = row['ROLE']
                ipi = row['IPI NUMBER']
                if ipi != '':
                    ipi = str(row['IPI NUMBER']).zfill(11)
                dict_owner = {"name": name,
                              "role": role,
                              "ipi": ipi}
                d['right_owners'].append(dict_owner)

            # Titles are not included in the right_owners loop deliberately in order to avoid errors in the consistency
            # of the data_sources. Drop duplicated titles and obtain cleaner data_sources has been the main reason.
            yield d
