from .productController import ProductApi
from .userController import UserApi


def initial_routes(api):
  api.add_resource(ProductApi, '/api/products')
  api.add_resource(UserApi, '/api/users')