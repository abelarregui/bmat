from flask import Flask, Response, request, json
from data_persistence.mongodb import MongoDB

app = Flask(__name__)


# Source:
# https://medium.com/@ishmeet1995/how-to-create-restful-crud-api-with-python-flask-mongodb-and-docker-8f6ccb73c5bc

@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')


@app.route('/musicalworks', methods=['GET'])
def mongo_read():
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
    app.run(debug=True, port=5001, host='0.0.0.0')
