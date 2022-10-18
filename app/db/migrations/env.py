from logging.config import fileConfig
from os import getenv

from sqlalchemy import engine_from_config
from sqlalchemy import pool

import pymysql
pymysql.install_as_MySQLdb()

from alembic import context

from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///travelers.sqlite3', echo=True)
#manage tables
base = declarative_base()

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.

# ak
# config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.

# ak
# fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata

target_metadata = None

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.

# ak
# DB_USER = getenv("DB_USER_MIG")
# DB_PASS = getenv("DB_PASSWORD_MIG")
# DB_HOST = getenv("DB_HOST")
# DB_PORT = getenv("DB_PORT")
# DB_NAME = getenv("DB_NAME")

# ak
# def run_migrations_online():
#     """Run migrations in 'online' mode.

#     In this scenario we need to create an Engine
#     and associate a connection with the context.
#     """
#     section = {}
#     url = "mysql://{}:{}@{}:{}/{}".format(DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME)
#     # Inject environment variable values into connection string
#     section["sqlalchemy.url"] = url
#     connectable = engine_from_config(
#         section,
#         prefix="sqlalchemy.",
#         poolclass=pool.NullPool,
#     )

#     with connectable.connect() as connection:
#         context.configure(connection=connection, target_metadata=target_metadata)

#         with context.begin_transaction():
#             context.run_migrations()


# run_migrations_online()

# new
Session = sessionmaker(bind=engine)
session = Session()
# i think this is where it is breaking, investigate tomorrow  LOOK AT THIS AND DELETE
class Travelers(base):
    __tablename__ = 'Travelers'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String)
    address = Column(String)
    creation_date = Column(String)

    def __init__(self, id, name, email, address, creation_date):
        self.id = id
        self.name = name
        self.email = email
        self.address = address
        self.creation_date = creation_date

base.metadata.create_all(engine)
insert_stuff = Travelers(1,'John','email@email.com','123 happy street', "20221005")
session.add(insert_stuff)
session.commit()