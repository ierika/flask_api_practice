from flask import Flask

from views import index


app = Flask(__name__)


# Routes
app.add_url_rule('/', 'index', index.index)
app.add_url_rule('/store/', 'store_list', index.get_store_list)
app.add_url_rule('/store/add/', 'store_add', index.add_store, methods=['POST'])
app.add_url_rule('/store/<string:name>/items/add/', 'store_items_add',
                 index.add_items, methods=['POST'])
app.add_url_rule('/store/<string:name>/', 'store_detail', index.get_store)


if __name__ == '__main__':
    app.run(port=5000)
