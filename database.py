import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# engine = create_engine('sqlite:///app.db')
# session_db = sessionmaker()
# session_db.configure(bind=engine)

DIALECT = 'oracle'
SQL_DRIVER = 'cx_oracle'
USERNAME = 'USERDB' #enter your username
PASSWORD = 'PASSWORD' #enter your password
HOST = 'localhost' #enter the oracle db host url
PORT = 1521 # enter the oracle port number
#SERVICE = 'your_oracle_service_name' # enter the oracle db service name
ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT)# + '/?service_name=' + SERVICE
engine = create_engine(ENGINE_PATH_WIN_AUTH)
session_db = sessionmaker()
session_db.configure(bind=engine)