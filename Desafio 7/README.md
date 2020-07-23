# Desafio ORM Queries

 Uma das coisas mais interessantes do framework Django é sem dúvidas o seu ORM.
  E o que o torna interessante é a sua simplicidade e objetividade quando se utiliza os
   Lookups para realizar consultas simples e até as complexas que envolvem join's. 
   Com base no desenho a seguir complete as funções para que façam as seguintes consultas usando o ORM do Django."
    
    Traga todos os uarios ativos, seu último login deve ser menor que 10 dias.
    Retorne a quantidade total de usuarios do sistema.
    Traga todos os usuarios com grupo = 'admin'.
    Traga todos os eventos com tipo debug.
    Traga todos os eventos do tipo critico de um usuário específico.
    Traga todos os agentes de associados a um usuário pelo nome do usuário.
    Traga todos os grupos que contenham alguem que possua um agente que possuem eventos do tipo information.


![orm](https://codenation-challenges.s3-us-west-1.amazonaws.com/python-11/challenge.png)
## Tópicos

Neste desafio você vai aprender:

- Uso correto do ORM do Django


## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

Sugestão, crie um projeto base com Django para testar as validações e o funcionamento da implementação.

    django-admin startproject ormchallenge
    cd ormchallenge
    django-admin startapp api
    django-admin createsuperuser
    python manage.py migrate
    python manage.py runserver
    
Agora acesse http://127.0.0.1:8000/admin use o usuário criado no processo para acessar a página de administração do Django.
