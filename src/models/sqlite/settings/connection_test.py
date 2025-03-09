from .connection import db_connection_handler

def test_connect_to_db():
  db_connection_handler.connect_to_db()
  assert db_connection_handler.get_engine() is not None
  