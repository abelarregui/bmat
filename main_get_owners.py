from data_persistence.mongodb import MongoDB
import pprint

mongo = MongoDB()

data = {"db": "bmat",
        "collection": "musicalworks",
        "iswc": ["T0426508306", "T0420889173"]
        }
musical_works = mongo.get_by_iswc(data)
for mw in musical_works:
    pprint.pprint(mw)
    # print(mw)
