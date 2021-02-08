import sys
sys.path.append('.')

from sqlalchemy.orm.exc import UnmappedInstanceError
from backend.dao.banned_category_dao import BannedCategoryDao
from backend.model.banned_category_model import BannedCategory
import pytest


class TestsCategorytDao:
    @pytest.fixture
    def create_instance(self):
        cat = BannedCategory('Categoria')
        return cat

    def test_instance(self):
        banned_category_dao = BannedCategoryDao()
        assert isinstance(banned_category_dao, BannedCategoryDao)

    def test_save(self, create_instance):
        banned_category_saved = BannedCategoryDao().save(create_instance)

        assert banned_category_saved.id_ is not None
        BannedCategoryDao().delete(banned_category_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            banned_category_saved = BannedCategoryDao().save('banned_category')

    def test_read_by_id(self, create_instance):
        banned_category_saved = BannedCategoryDao().save(create_instance)
        banned_category_read = BannedCategoryDao().read_by_id(banned_category_saved.id_)

        assert isinstance(banned_category_read, BannedCategory)
        BannedCategoryDao().delete(banned_category_read)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            banned_category_read = BannedCategoryDao().read_by_id('testess')

    def test_read_all(self):
        banned_category_read = BannedCategoryDao().read_all()

        assert isinstance(banned_category_read, list)

    def test_delete(self, create_instance):
        banned_category_saved = BannedCategoryDao().save(create_instance)
        banned_category_read = BannedCategoryDao().read_by_id(banned_category_saved.id_)
        BannedCategoryDao().delete(banned_category_read)
        banned_category_read = BannedCategoryDao().read_by_id(banned_category_saved.id_)

        assert banned_category_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            BannedCategoryDao().delete('teste')
