from typing import Dict
from src.models.sqlite.entities.pets import PetsTable
from src.controllers.pet_list_controller import PetListController

class MockPetRepository():
  def list_pets(self) -> Dict:
    return [
      PetsTable(name="Rex", id=4),
      PetsTable(name="Fido", id=55)
    ]

def test_list_pets() -> None:
  controller = PetListController(MockPetRepository())
  response = controller.list_pets()

  expected_response = {
    "data": {
      "type": "Pets",
      "count": 2,
      "attributes": [
        {"name": "Rex", "id": 4},
        {"name": "Fido", "id": 55}
      ],
    }
  }

  assert response == expected_response
