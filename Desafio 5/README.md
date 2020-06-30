# Desafio Data Design

   
Um modelo é a única e definitiva fonte de dados sobre os seus dados.
Ele contém os campos e métodos essenciais para manipular os dados que você está armazenando.  Em geral, cada modelo mapeia uma tabela no seu banco de dados.

Com base no desenho abaixo, modele esse relacionamento com os *models* do Django.

![](https://codenation-challenges.s3-us-west-1.amazonaws.com/python-9/challenge.png)

    Obs:
    Os campos que dever ser validados:
    User.email (validação de e-mail)
    User.password (a senha não pode ser menor do que 8 caráteres)
    Agent.address (validação IPV4)
    Event.level possiveis opções (CRITICAL, DEBUG, ERROR, WARNING, INFO)
    
## Tópicos

Neste desafio você vai aprender:

- Modelagem de dados
- Modelos Django
- Validações


## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

Para resolver este desafio faça os passos abaixo:

- Crie um projeto base com Django para testar as validações e o funcionamento da implementação.


	django-admin startproject datadesign
	cd datadesign
	django-admin startapp api
	python manage.py migrate
    python manage.py createsuperuser
	python manage.py runserver

Agora acesse http://127.0.0.1:8000/admin use o usuário criado no 
processo para acessar a página de administração do Django.

- Implemente os models.py conforme a modelagem de dados. (*datadesign/api/models.py*)
- Rode o comando para criar as migrations.
    
    python manage.py makemigrations
    python manage.py migrate


A implementação deve ser feita e no arquivo **api/models.py** ,
copie o conteúdo do models do seu projeto para o diretório api.
Exemplo: **cp datadesign/api/models.py > api/models.py** (ou use o gerenciador de arquivos do seu sistema operacional)
Substitua o arquivo de banco de dados (*datadesign/db.sqlite3*).

Obs: Verifique o arquivo de settings e o `DATABASES['NAME']`.

