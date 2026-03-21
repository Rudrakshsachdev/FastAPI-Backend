# this import is done to create a connection to the database using SQLAlchemy. The create_engine function is used to create an engine object that can be used to interact with the db.
from sqlalchemy import create_engine

# the sessionmaker function is used to create a session factory that can be used to create sessions for interacting with the db.
from sqlalchemy.orm import sessionmaker

from core.config import DATABASE_URL

# here, we are intializing the database engine using the DATABASE_URL from the config file. This will allow us to connect to the database and perform operations on it.
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# here, we are creating a session factory using the sessionmaker function. We set autocommit to False and autoflush to False to ensure that changes to the database are not automatically committed or flushed. We also bind the session factory to the engine we created earlier, so that it can be used to interact with the database.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)