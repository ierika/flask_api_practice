from flask import jsonify, request


# Sample data
stores = [
    {
        'name': 'Store One',
        'items': [],
    },
]


def make_response(success=True, message=None, **kwargs):
    """Make a standard API response"""
    return jsonify({
        'success': success,
        'message': message,
        **kwargs,
    })


def index():
    return '<h1>Index page</h1>'


def get_store_list():
    """Get store list"""
    return make_response(success=True, stores=stores)


def add_store():
    """Add store"""
    post_data = request.get_json()

    if post_data.get('name'):
        name = post_data['name']
        store = {
            'name': name,
            'items': [],
        }
        stores.append(store)
        return make_response(message='Store has been added', store=store)

    return make_response(success=False, message='No store to add')


def get_store(name):
    """Get specific store"""
    for store in stores:
        if store['name'] == name:
            return make_response(store=store)

    return make_response(success=False,
                         message='No store called {} was found'.format(name))


def add_items(name):
    """Add items to store"""
    req = request.get_json()
    items = req.get('items')

    if items:
        for store in stores:
            if store['name'] == name:
                items = [i for i in items if i not in store['items']]
                store['items'] += items
                return make_response(store=store)

    else:
        return make_response(success=False, message='No items to add')
