from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):
  @abstractmethod
  def detele(self, name: str) -> None:
    pass
