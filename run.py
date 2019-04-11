from flask import Flask
from flask_restful import Api

from views import index
from api.v1 import dogs


app = Flask(__name__)
api = Api(app)

# Request middleware

# Routes
app.add_url_rule('/', 'index', index.index)
app.add_url_rule('/store/', 'store_list', index.get_store_list)
app.add_url_rule('/store/add/', 'store_add', index.add_store, methods=['POST'])
app.add_url_rule('/store/<string:name>/items/add/', 'store_items_add',
                 index.add_items, methods=['POST'])
app.add_url_rule('/store/<string:name>/', 'store_detail', index.get_store)

# API via Flask RESTful module
api.add_resource(dogs.Dogs, '/api/v1/dogs')
api.add_resource(dogs.Dog, '/api/v1/dog')

# Response middleware
# Exception handler


if __name__ == '__main__':
    app.run(port=5000)
