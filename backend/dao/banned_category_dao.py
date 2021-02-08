from backend.model.banned_category_model import BannedCategory
from backend.dao.base_dao import BaseDao


class BannedCategoryDao(BaseDao):
    def __init__(self):
        super().__init__(BannedCategory)
