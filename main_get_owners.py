from data_persistence.mongodb import MongoDB
import pprint

print('##################')
print('Get process starts')
print('##################')

# Connect to the data base (MongoDB)
print("* Connecting with the data base (MongoDB)... ", end='', flush=True)
mongo = MongoDB()
print("OK")

# Query data from bmat and musicalworks collection
data = {"db": "bmat",
        "collection": "musicalworks",
        "iswc": ["T0426508306", "T0420889173"]
        }

print("* Querying data... ", end='', flush=True)
musical_works = mongo.get_by_iswc(data)
print("OK")
for mw in musical_works:
    pprint.pprint(mw)
    # print(mw)

print('##################')
print('ETL process ends')
print('##################')
