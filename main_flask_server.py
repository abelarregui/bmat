from flask import Flask, Response, request, json
from data_persistence.mongodb import MongoDB

app = Flask(__name__)


# Reference:
# https://medium.com/@ishmeet1995/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc

@app.route('/')
def base():
    """
    Base webpage: status UP
    :return:
    """
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/musicalworks', methods=['GET'])
def mongo_read():
    """
    GET endpoint. A dictionary is needed for input parameter. Example:
        {
        "db": "bmat",
        "collection": "musicalworks",
        "iswc": ["T0426508306", "T0420889173"]
        }
    :return: json with right owners info for the given iswc's
    """
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    mongo = MongoDB()
    response = mongo.get_by_iswc(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=5001, host='127.0.0.1')
