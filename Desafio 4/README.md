# Desafio sobre Backend Skills

 O JSON Web Token (JWT) é um padrão aberto (RFC 7519) que define uma maneira compacta e 
 independente de transmitir com segurança informações entre as partes como um objeto JSON. 
 Essas informações podem ser verificadas e confiáveis ​​porque são assinadas digitalmente. 
 As JWTs podem ser assinadas usando um segredo (com o algoritmo HMAC) ou um par de chaves 
 pública / privada usando RSA ou ECDSA. 
 
 Complete a funções para rertornar um json web token, gerado usando o algoritmo HS256, que contenha a seguinte informação **{"language": "Python"}**,
 com a palavra secreta **acelera**, complete a função para decifrar as informações tratando a exceção de quando a assinatura for inválida
 devendo retornar o seguinte dicionário {"error": 2}.
 Não havendo erro, retornar a informação decifrada.


## Tópicos

Neste desafio você vai aprender:

- Encode JWT Tokens
- Decode Jwt Tokens


## Requisitos

Você precisará de python 3.6 (ou superior) e do gerenciador de pacotes pip.

O recomendado é você utilizar um [ambiente virtual](https://pythonacademy.com.br/blog/python-e-virtualenv-como-programar-em-ambientes-virtuais). Para isto, execute os comandos como no exemplo abaixo:

    pip3 install virtualenv
    virtualenv venv -p python3
    source venv/bin/activate 
    pip install -r requirements.txt

Ao terminar o desafio, você pode sair do ambiente criado com o comando `deactivate`

## Estudos Adicionais

- https://jwt.io/
- https://pyjwt.readthedocs.io/en/latest/usage.html#encoding-decoding-tokens-with-hs256
- https://medium.com/@gustavolpss/json-web-tokens-jwt-em-python-c76fb34d8d9
- https://pypi.org/project/PyJWT/1.4.0/


