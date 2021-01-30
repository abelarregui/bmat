import pandas as pd
import numpy as np
from .aux_functions import clean_string_iswc


class CsvSourceType1:

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
        self.df = pd.read_csv(path_file, converters={'IPI NUMBER': str})

    def check_consistency(self):
        """

        """
        # TODO
        df = self.df
        check_iswc = df['ISWC'].unique()
        check_ot = df['ORIGINAL TITLE'].unique()
        check_iswc = df['ISWC'].unique()

    def transform_to_list_dict(self):
        """

        :return:
        """
        df_raw = self.df
        df_raw = df_raw.fillna('')
        list_works = []
        # As the specification document says, ID SOCIETY will be PK, for this reason, this column is used to make a loop
        # grouping for musical work
        for id_work, df in df_raw.groupby('ID SOCIETY'):
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

            # AlternativeTitles: All unique values are calculated. Then, new dictionaries are added to the list
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
            list_works.append(d)

        return list_works

    def save_to_file_as_dict(self, path_output_file):
        """

        :rtype: object
        :param path_output_file: 
        """
        list_works_dict = self.transform_to_list_dict()
        with open(path_output_file, 'w') as f:
            f.write(str(list_works_dict))
        return list_works_dict


class CsvSourceType2:
    pass
