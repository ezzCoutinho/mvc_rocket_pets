import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.models.sqlite.repositories.people_repository import PeopleRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_list_pets():
  repo = PetsRepository(db_connection_handler)
  response = repo.list_pets()
  print(response)

@pytest.mark.skip(reason="interacao com o banco")
def test_delete_pet():
  name = "belinha"
  repo = PetsRepository(db_connection_handler)
  repo.delete_pets(name)

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_person():
  person = 1

  repo = PeopleRepository(db_connection_handler)
  response = repo.get_person(person)
  print()
  print(response)
  print(response.pet_name)
