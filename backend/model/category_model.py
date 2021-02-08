from sqlalchemy.orm import validates
from sqlalchemy import String, Column
from backend.model.base_model import BaseModel
from backend.utils.validators import *


class Category(BaseModel):
    __tablename__ = 'category'

    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=True)

    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description

    @validates('name')
    def validate_name(self, key, name):
        name = validate_type(name, str, key)
        name = validate_not_empty(name, key)
        return validate_len(name, 100, key)

    @validates('description')
    def validate_description(self, key, description):
        description = validate_type(description, str, key)
        return validate_len(description, 100, key)