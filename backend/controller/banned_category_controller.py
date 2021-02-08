from flask_restful import fields, marshal_with

from backend.dao.banned_category_dao import BannedCategoryDao
from backend.model.banned_category_model import BannedCategory
from backend.controller.base_controller import BaseController


class BannedCategoryController(BaseController):
    fields = {
        "id_": fields.Integer,
        "name": fields.String
    }

    def __init__(self):
        self.__dao = BannedCategoryDao()
        self.__model_type = BannedCategory

        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def get(self, id=None):
        return super().get(id)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def put(self, id):
        return super().put(id)

    @marshal_with(fields)
    def delete(self, id):
        return super().delete(id)