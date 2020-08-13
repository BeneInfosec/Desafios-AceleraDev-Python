# Desafio RESTful API Modeling Language (RAML)

Projetar uma API é fácil. Mas projetar uma API que tenha vida longa e que seus usuários 
adorem, bem, isso é um pouco mais difícil. Mas com a RAML, você pode aproveitar todo o 
ciclo de vida da API, o que significa que você pode projetar sua API visualmente, 
testá-la e obter feedback do usuário sem precisar escrever uma única linha de código.

Precisamos modelar alguns endpoints para que duas equipes Frontend e Backend possam trabalhar em paralelo. As especificações
da API precisam estar bem definidas e validadas, então crie um documento usando a especificação RAML 1.0, que de norte
para que as duas equipes possam trabalhar ao mesmo tempo, a equipe Backend na modelagem, armazenamento e fornecimento dos dados
e o Frontend para consumir estes dados através destes endpoints.


Com base no desenho abaixo escreva a especificação da API usando RAML para gerenciar as entidades
`User, Group, Agent, Event`. Todas precisam ter um endpoint para criação, listagem total, 
listagem individial, remoção e atualização, seguintdo os padrões REST e retornando corretamente os 
códigos HTTP.

Implemente a solução dentro da string _doc_ dentro do arquivo main.py

A API deve ter usar autenticação com Token JWT.
Declare os types no mesmo arquivo, Ex:

    types:
      Auth:
        type: object
        discriminator: token
        properties:
          token : string
      Agent:
        type: object
        .
        .
        .
    

 Endpoints
 
       /auth/token
       /agents
       /agents/{id}
       /agents/{id}/events
       /agents/{id}/events/{id}
       /groups
       /groups/{id}
       /users
       /users/{id}

![orm](https://codenation-challenges.s3-us-west-1.amazonaws.com/python-12/Challenge.png)
## Tópicos

Neste desafio você vai aprender:

- Design de API
- Especificação RAML 1.0
- Conceitos sobre REST



## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

Sugestão, fique a vontade para usar editores online para auxiliar seu trabalho, o importante é que a api fique bem documentada.