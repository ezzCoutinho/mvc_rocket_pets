from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

class DBConnectionHandler:
  def __init__(self) -> None:
    self.__connection_string = "sqlite:///storage_init.db"
    self.__engine = None

  def connect_to_db(self) -> None:
    self.__engine = create_engine(self.__connection_string)

  def get_engine(self) -> Engine:
    return self.__engine


db_connection_handler = DBConnectionHandler()
  