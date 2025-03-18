from src.models.sqlite.interfaces.pets_repository_interface import PetsRepositoryInterface

class PetDeleterController:
  def __init__(self, pets_repository_interface: PetsRepositoryInterface) -> None:
    self.__pets_repository_interface = pets_repository_interface

  def detele(self, name: str) -> None:
    response = self.__delete_pets_in_db(name)

    return response

  def __delete_pets_in_db(self, name: str) -> None:
    pet = self.__pets_repository_interface.delete_pets(name)
    if not pet:
      raise Exception("Pet not found!")

    return pet
