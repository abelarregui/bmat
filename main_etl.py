from data_sources.csv_source import CsvSourceType1
from data_persistence.mongodb import MongoDB


path_csv = r'C:\Users\abel\Jupyter\bmat\data/db_works_test.csv'
csv_data = CsvSourceType1(path_csv)
# csv_data.check_consistency()
list_works_dict = csv_data.transform_to_list_dict()

data = {"db": "bmat",
        "collection": "musicalworks",
        "list_works_dict": list_works_dict
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

