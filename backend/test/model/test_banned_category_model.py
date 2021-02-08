import sys
sys.path.append('.')

from backend.model.banned_category_model import BannedCategory
from backend.model.base_model import BaseModel
import pytest

class TestBannedCategoryModel:
    name = "Agrotoxico"


    def test_istance(self):
        banned_category = BannedCategory(self.name)
        assert isinstance(banned_category, BannedCategory)
        assert isinstance(banned_category, BaseModel)


    def test_empty_name(self):
        with pytest.raises(ValueError):
            banned_category = BannedCategory("")


    def test_name_length(self):
        with pytest.raises(ValueError):
            banned_category = BannedCategory("*" * 101)


    def test_name_type(self):
        with pytest.raises(TypeError):
            banned_category = BannedCategory(101)


