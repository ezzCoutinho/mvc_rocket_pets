from typing import Dict
from abc import ABC, abstractmethod

class PetListControllerInterface(ABC):
  @abstractmethod
  def list_pets(self) -> Dict:
    pass
