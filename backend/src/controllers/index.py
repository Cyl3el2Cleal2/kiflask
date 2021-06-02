from .productController import ProductApi
from .userController import UserApi
from .orderController import OrderApi


def initial_routes(api):
  api.add_resource(ProductApi, '/api/products', '/api/products/<id>')
  api.add_resource(UserApi, '/api/users', '/api/users/<id>')
  api.add_resource(OrderApi, '/api/orders', '/api/orders/<id>')