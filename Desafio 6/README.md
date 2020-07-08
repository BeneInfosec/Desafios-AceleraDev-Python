# Desafio REST API

REST significa Representational State Transfer. Em português, 
Transferência de Estado Representacional. Trata-se de uma abstração da 
arquitetura da Web. Resumidamente, o REST consiste em princípios/regras/constraints
 que, quando seguidas, permitem a criação de um projeto com interfaces bem definidas. 
 Desta forma, permitindo, por exemplo, que aplicações se comuniquem.

Utilizando os conceitos apresentados nos conteúdo de apoio propostos, utilizando se de boas praticas no desenvolvimento de software,
 implemente uma aplicação utilizando Django e Django REST Framework.

Essa aplicação é uma API que funcionará como um serviço lambda, implemente views baseadas em funções, que retornarão o resultado das funções em um formato json.

Função 1) A função a ser implementada em um endpoint recebe um request com POST com um json, que contem uma lista de numeros, a função deve 
deve retornar uma lista com os numeros ordenados pela quantidade de vezes que eles aparecem na lista.

    Exemplo:
    POST data = {"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}
    Response = {"solution":[3 ,3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]}
    Função =   solution([2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]) == [3, 3, 3, 3, 2, 2, 2, 5, 5, 12, 12, 4]]



## Tópicos

Neste desafio você vai aprender:

- Django Rest Framework
  - Serialization
  - Requests and responses
  - Function based views
  - Viewsets and routers


## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

Sugestão: Crie um projeto base com Django para testar as validações e o funcionamento da implementação.


	django-admin startproject restapi
	cd restapi
	django-admin startapp api
	python manage.py createsuperuser
	python manage.py migrate
	python manage.py runserver
    
Para testar a aplicação
    
    curl -X POST http://127.0.0.1:8000/lambda/ -H "Content-Type: application/json" -d '{"question": [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12, 5]}'
    response {"solution":[3,3,3,3,2,2,2,5,5,12,12,4]}

A implementação deve ser feita no arquivo *api/views.py* ,
copie o conteúdo das views do seu projeto para o diretório api. Exemplo *cat restapi/api/views.py > api/views.py* (ou use o gerenciador de arquivos do seu sistema operacional) 


## Conteudos Auxiliares:
http://pythonclub.com.br/django-rest-framework-requests-responses.html
https://www.it-swarm.dev/pt/python/como-receber-dados-json-usando-solicitacao-http-post-em-django-1.6/1047265548/
https://www.django-rest-framework.org/api-guide/views/#api_view
https://www.geeksforgeeks.org/python-sort-list-elements-by-frequency/
