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


## 17/03

Hoje desenvolvemos e implementamos quatro novos controllers:
- PersonCreator: responsável por criar novas pessoas no sistema para adoção de pets
- PersonFinder: permite encontrar uma pessoa específica através do seu ID
- PetList: responsável por listar todos os pets cadastrados no sistema
- PetDeleter: permite remover um pet do sistema através do seu nome

Além disso, criamos testes unitários para cada um desses controllers, garantindo seu funcionamento adequado.


## 18/03

Hoje implementamos a interface base para todos os controllers do nosso padrão MVC (Model-View-Controller), estabelecendo um contrato comum para padronizar a estrutura dos controllers no projeto.


## 20/03

Hoje implementamos a view do nosso projeto, criando interfaces e views para cada controller. Além disso, desenvolvemos a interface base para todas as views do nosso padrão MVC.


## 21/03

Hoje implementamos a pasta main, que contém a estrutura principal da aplicação. Nela, criamos o padrão Composite que integra as três camadas da arquitetura MVC (Model, View e Controller) de forma organizada e com responsabilidades bem definidas. Desenvolvemos três rotas:
- Uma rota de teste para validar a configuração
- Duas rotas para o PersonController:
  - POST /people: para criar uma nova pessoa
  - GET /people/{id}: para buscar uma pessoa específica pelo ID


## 22/03

Hoje implementamos duas novas rotas para o gerenciamento de pets:
- GET /pets: lista todos os pets cadastrados no sistema
- DELETE /pets/{name}: remove um pet específico através do seu nome

Também realizamos ajustes importantes no código:
- Removemos uma exception desnecessária no PetDeleterController
- Corrigimos a validação de deleção para seguir o padrão HTTP 204 (No Content)
- Implementamos os composers necessários para integrar as camadas Model, View e Controller


## 23/03

Hoje implementamos melhorias significativas no tratamento de erros da aplicação:

1. Criação de Erros Personalizados:
   - Desenvolvemos classes de erro customizadas (HttpBadRequest, HttpNotFound e HttpunprocessableEntity)
   - Implementamos respostas padronizadas para cada tipo de erro
   - Integramos os erros personalizados no PersonFinderController e PersonCreatorController

2. Validação de Dados com Pydantic:
   - Adicionamos a biblioteca Pydantic para validação de dados
   - Implementamos schemas para validar automaticamente os dados de entrada

Essas mudanças melhoram a robustez da aplicação e fornecem feedback mais claro aos usuários quando ocorrem erros.


## 24/03

Hoje focamos em melhorar a qualidade e confiabilidade do nosso código:

1. Testes de Integração:
   - Desenvolvemos testes de integração para o PersonCreatorController

2. Validação na View:
   - Implementamos a validação Pydantic no PersonCreatorView

Essas implementações aumentam a confiabilidade do sistema e garantem que a criação de pessoas funcione conforme o esperado.


## 26/03

Hoje concluímos o projeto com as seguintes implementações:

1. Centralização do Tratamento de Erros:
   - Implementamos o ErrorController para gerenciar todos os erros da aplicação
   - Padronizamos as respostas de erro em todas as rotas
   - Integramos o tratamento de erros com os tipos HTTP personalizados (BadRequest, NotFound, UnprocessableEntity)

2. Finalização do Módulo:
   - Revisamos e testamos todas as funcionalidades implementadas
   - Garantimos que todas as rotas estão utilizando o tratamento de erros centralizado
   - Verificamos a cobertura de testes e documentação

Com essas implementações, finalizamos o módulo com uma arquitetura robusta e bem estruturada, seguindo as melhores práticas de desenvolvimento.