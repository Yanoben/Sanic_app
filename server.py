from databases import Database
from sanic import Sanic
from sanic.response import json
# from sqlalchemy.sql import select
# from sqlalchemy.views import CreateView, DropView

from table import products, users, checkes

app = Sanic("sanic_app")


def setup_database():
    app.db = Database('postgresql://postgres:postgres@localhost/postgres')

    @app.listener('after_server_start')
    async def connect_to_db(*args, **kwargs):
        await app.db.connect()

    @app.listener('after_server_stop')
    async def disconnect_from_db(*args, **kwargs):
        await app.db.disconnect()


@app.route('/')
async def index(request):
    return json({
        'hello': 'world'
    })


@app.route('/products')
async def get_products(request):
    query = products.all()
    return json({
        'query': type(query)
    })
    # rows = await request.app.fetch_all(query)
    # return json({
    #     'products': [{row['title']: row['title']} for row in rows]
    # })


# @app.get("/products")
# async def products(request):
#     products = [
#         {"title": "product_a", "price": 10.0},
#         {"title": "product_b", "price": 5.0},
#     ]
#     return json(products)


if __name__ == '__main__':
    setup_database()
    app.run(host='0.0.0.0',
            port=8000,
            debug=True,
            auto_reload=True,)
