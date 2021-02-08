from flask import Flask
from flask_restful import Api

from backend.controller.category_controller import CategoryController

app = Flask(__name__)
api = Api(app)

api.add_resource(CategoryController, '/api/category', endpoint='categories')
api.add_resource(CategoryController, '/api/category/<int:id>', endpoint='category')


@app.route('/')
def index():
    return 'Bem Vindo!!!'


app.run(debug=True)