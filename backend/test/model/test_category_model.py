import sys
sys.path.append('.')

from backend.model.category_model import Category
from backend.model.base_model import BaseModel
import pytest

class TestCategoryModel:
    name = "Bebida"
    description = "Nacional"


    def test_istance(self):
        category = Category(self.name, self.description)
        assert isinstance(category, Category)
        assert isinstance(category, BaseModel)


    def test_empty_name(self):
        with pytest.raises(ValueError):
            categories = Category("", self.description)


    def test_name_length(self):
        with pytest.raises(ValueError):
            categories = Category("*" * 101, self.description)


    def test_name_type(self):
        with pytest.raises(TypeError):
            categories = Category(101, self.description)


    def test_description_length(self):
        with pytest.raises(ValueError):
            categories = Category(self.name, '*' * 201)


    def test_description_type(self):
        with pytest.raises(TypeError):
            categories = Category(self.name, 201)