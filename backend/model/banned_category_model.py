from sqlalchemy.orm import validates
from sqlalchemy import String, Column
from backend.model.base_model import BaseModel


class BannedCategory(BaseModel):
    __tablename__ = 'banned_category'

    name = Column('name', String(length=100), nullable=False)

    def __init__(self, name: str) -> None:
        self.name = name

    @validates('name')
    def validate_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        if not name:
            raise ValueError("Name can't be null!")
        if len(name) > 100:
            raise ValueError("Name must be 100 characters or less!")
        return name
