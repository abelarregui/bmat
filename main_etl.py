import pprint
from data_sources.csv_source import CsvSourceType1
from data_persistence.mongodb import MongoDB

print('##################')
print('ETL process starts')
print('##################')

# Read RAW data
path_csv = r'data_files_raw/db_works_test.csv'
print("* Reading RAW data... ", end='', flush=True)
csv_data = CsvSourceType1(path_csv)
print("OK")

# Print consistency report
csv_data.check_consistency()

# Transform data to list of dictionaries
print("* Transforming data... ", end='', flush=True)
list_works_dict = csv_data.transform_to_list_dict()
print("OK")
pprint.pprint(list_works_dict)

# Ingest MongoDB with the data
print("* Connecting with the data base (MongoDB)... ", end='', flush=True)
mongo = MongoDB()
print("OK")

data = {"db": "bmat",
        "collection": "musicalworks",
        "list_dict": list_works_dict
        }
# print(list_works_dict)
print("connecting with mongo")
mongo = MongoDB()
# for db in mongo.client.list_databases():
#     print(db)

result_insert = mongo.insert_many(data)
if result_insert:
    print(result_insert.inserted_ids)
else:
    print("No data added")

print('##################')
print('ETL process ends')
print('##################')
