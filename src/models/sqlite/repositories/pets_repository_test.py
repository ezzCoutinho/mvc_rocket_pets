from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.repositories.pets_repository import PetsRepository

class MockConnection:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock(
      data=[
        (
          [mock.call.query(PetsTable)], # query
          [
            PetsTable(name="dog", Type="dog"),
            PetsTable(name="cat", Type="cat")
           ] # resultado
        )
      ]
    )

  def __enter__(self) -> 'MockConnection':
    return self

  def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    pass

def test_list_pets():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  assert response[0].name == "dog"
  assert response[1].name == "cat"
 