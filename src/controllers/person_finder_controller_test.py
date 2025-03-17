#pylint: disable=unused-argument
from src.controllers.person_finder_controller import PersonFinderController

class MockPerson():
  def __init__(self, first_name: str, last_name: str, pet_name: str, pet_type: str) -> None:
    self.first_name = first_name
    self.last_name = last_name
    self.pet_name = pet_name
    self.pet_type = pet_type

class MockPeopleRepository():
  def get_person(self, person_id: int) -> None:
    return MockPerson(
      first_name="Fulano",
      last_name="de Tal",
      pet_name="Furão",
      pet_type="Cachorro"
      )

def test_find() -> None:
  controller = PersonFinderController(MockPeopleRepository())
  response = controller.find(123)

  expected_response = {
    "data": {
        "type": "Person",
        "count": 1,
        "attributes": {
          "first_name": "Fulano",
          "last_name": "de Tal",
          "pet_name": "Furão",
          "pet_type": "Cachorro"
        }
      }
  }

  assert response == expected_response
