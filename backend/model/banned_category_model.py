from sqlalchemy.orm import validates
from sqlalchemy import String, Column
from backend.model.base_model import BaseModel
from backend.utils.validators import *


class BannedCategory(BaseModel):
    __tablename__ = 'banned_category'

    name = Column('name', String(length=100), nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_len(name, 100, key)
