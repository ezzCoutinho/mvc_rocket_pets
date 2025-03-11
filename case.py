class AlgumaCoisa:
  def __enter__(self) -> None:
    print("Estou entrando")

  def __exit__(self, exc_type, exc_val, exc_tb) -> None:
    print("Estou saindo")

with AlgumaCoisa() as something:
  print("estou no meio")
