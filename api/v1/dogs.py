from flask_restful import Resource
from flask import request


dogs = []


class Dogs(Resource):
    def get(self):
        return {'dogs': dogs}


class Dog(Resource):
    def get(self):
        pass

    def post(self):
        request_data = request.get_json()
        name = request_data.get('name')
        breed = request_data.get('breed')

        if name and breed:
            dog = {
                'name': name,
                'breed': breed,
            }
            dogs.append(dog)
            return {'dog': dog}

    def put(self, name):
        pass

    def delete(self, name):
        pass
