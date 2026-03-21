# this import is used to create a base class for our SQLAlchemy models. The declarative_base function from SQLAlchemy's ORM module is called to create this base class, which will be used as a parent class for all our database models.
from sqlalchemy.orm import declarative_base

Base = declarative_base()