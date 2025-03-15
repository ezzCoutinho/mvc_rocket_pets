from unittest import mock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound
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

class MockConnectionNoResult:
  def __init__(self) -> None:
    self.session = UnifiedAlchemyMagicMock()
    self.session.query.side_effect = self.__raise_no_result_found

  def __raise_no_result_found(self, *args, **kwargs):
    raise NoResultFound("No result found")

  def __enter__(self) -> 'MockConnectionNoResult':
    return self

  def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    pass

def test_list_pets():
  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.all.assert_called_once()
  mock_connection.session.filter.assert_not_called()

  assert response[0].name == "dog"
  assert response[1].name == "cat"

def test_delete_pet():
  name = "dog"

  mock_connection = MockConnection()
  repo = PetsRepository(mock_connection)
  repo.delete_pets(name)

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.filter.assert_called_once_with(PetsTable.name == "dog")
  mock_connection.session.delete.assert_called_once()
  mock_connection.session.commit.assert_called_once()

def test_list_pets_no_result():
  mock_connection = MockConnectionNoResult()
  repo = PetsRepository(mock_connection)
  response = repo.list_pets()

  mock_connection.session.query.assert_called_once_with(PetsTable)
  mock_connection.session.all.assert_not_called()
  mock_connection.session.filter.assert_not_called()

  assert response == []

def test_delete_pet_error():
  mock_connection = MockConnectionNoResult()
  repo = PetsRepository(mock_connection)

  with pytest.raises(Exception):
    repo.delete_pets("petName")

  mock_connection.session.rollback.assert_called_once()
