from .productController import ProductApi
from .userController import UserApi
from .orderController import OrderApi
from .stockController import StockApi
from .machineController import MachineApi


def initial_routes(api):
  api.add_resource(ProductApi, '/api/products', '/api/products/<id>')
  api.add_resource(UserApi, '/api/auth')
  api.add_resource(OrderApi, '/api/orders', '/api/orders/<id>')
  api.add_resource(StockApi, '/api/stocks', '/api/stocks/<id>')
  api.add_resource(MachineApi, '/api/machines', '/api/machines/<id>')