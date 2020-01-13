from flask_restful import Api, Resource

class Movies(Resource):
    def get(self):
        return {'Name': 'Star Shrek'}
