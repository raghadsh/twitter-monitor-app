from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse
app = Flask(__name__)
CORS(app)
api = Api(app)


class Get_Trends(Resource):
    def get(self):
        return  "test"

#os.system("java -cp fgw.jar farasa.gateway.LemmatizerEntryPoint")
api.add_resource(Get_Trends, "/Get_Trends/")



if __name__ == '__main__':
  app.run()

