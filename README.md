## Dia 09/03

Hoje aprendemos sobre a importância do pylint em projetos de equipe e o integramos ao pre-commit. Isso garante que, caso haja um erro detectado pelo pylint, o commit não será enviado para o GitHub. Além disso, criamos nosso banco de dados.

## 10/03

Hoje criamos testes de integração com o banco de dados, fizemos algumas modificações no pylint, criamos os modelos de People e Pets, utilizamos o SQLAlchemy para ser declarativo em nossa base e, por fim, fizemos uma listagem de pets.

## 11/03

Hoje aplicamos skips em alguns testes do pytest, criamos um método para deletar um pet específico e criamos testes unitários para o método list_pets.

## 14/03

Hoje finalizamos os testes de integração dos pets e iniciamos os testes de integração para people. Além disso, implementamos um método que permite listar qual pessoa adotou um determinado pet, realizando a busca através do ID do pet adotado.

## 15/03

Hoje criamos interfaces para as tabelas do repositório e as integramos com o banco de dados. Em seguida, desenvolvemos o controller PersonCreator na pasta controllers, responsável por criar uma nova pessoa no sistema, implementando os métodos necessários e suas respectivas validações.