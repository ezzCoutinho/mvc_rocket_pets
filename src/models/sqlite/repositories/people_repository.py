from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import PeopleTable

class PeopleRepository:
  def __init__(self, db_connection) -> None:
    self.__db_connection = db_connection

  def list_people(self) -> List[PeopleTable]:
    with self.__db_connection as database:
      try:
        people = database.session.query(PeopleTable).all()
        return people
      except NoResultFound:
        return []
