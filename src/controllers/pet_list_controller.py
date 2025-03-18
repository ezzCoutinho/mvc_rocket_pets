from typing import Dict, List
from src.models.sqlite.interfaces.pets_repository_interface import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable

class PetListController:
  def __init__(self, pets_repository_interface: PetsRepositoryInterface) -> None:
    self.__pets_repository_interface = pets_repository_interface

  def list_pets(self) -> Dict:
    pets = self.__get_pets_in_db()
    response = self.__format_response(pets)

    return response

  def __get_pets_in_db(self) -> List[PetsTable]:
    pet = self.__pets_repository_interface.list_pets()
    if not pet:
      raise Exception("Pet not found!")

    return pet

  def __format_response(self, pets: List[PetsTable]) -> Dict:
    formatted_pets = []
    for pet in pets:
      formatted_pets.append(
        {
        "name": pet.name,
        "id": pet.id,
        }
      )

    return {
      "data": {
        "type": "Pets",
        "count": len(formatted_pets),
        "attributes": formatted_pets,
      }
    }
