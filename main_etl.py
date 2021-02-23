import pprint
from data_sources.csv_source import CsvSourceType
from data_persistence.mongodb import MongoDB


def main():
    """
    ETL main function
    """
    print('##################')
    print('ETL process starts')
    print('##################')

    # Read RAW data
    path_csv = r'data_files_raw/db_works_test.csv'
    print("* Reading RAW data... ", end='', flush=True)
    csv_data = CsvSourceType(path_csv)
    print(csv_data.unique_id_society)
    parsed_data = csv_data.parsed_data()

    # Ingest MongoDB with the data
    print("* Connecting with the data base (MongoDB)... ", end='', flush=True)
    mongo = MongoDB()
    print("OK")

    for doc in parsed_data:
        print(doc)
        data = {"db": "bmat",
                "collection": "musicalworks",
                "document": doc
                }
        mongo.insert(data)


if __name__ == '__main__':
    main()
