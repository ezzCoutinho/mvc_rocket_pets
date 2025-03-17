import pytest
from src.controllers.person_creator_controller import PersonCreatorController

class MockPeopleRepository:
  def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
    pass

def test_create() -> None:
  person_infor = {
    "first_name": "Fulano",
    "last_name": "de Tal",
    "age": 20,
    "pet_id": 123
  }

  controller = PersonCreatorController(MockPeopleRepository())
  response = controller.create_person(person_infor)

  assert response["data"]["type"] == "Person"
  assert response["data"]["count"] == 1
  assert response["data"]["attributes"] == person_infor

def test_create_error() -> None:
  person_infor = {
    "first_name": "Fulano123",
    "last_name": "de Tal",
    "age": 20,
    "pet_id": 123
  }

  controller = PersonCreatorController(MockPeopleRepository())

  with pytest.raises(Exception):
    controller.create_person(person_infor)
