import jwt


data = { #Payload
    'language': 'Python'
}

secret = 'acelera'

dic = {'error': 2}

def create_token(data, secret):
    return jwt.encode(data, secret, algorithm='HS256')


def verify_signature(token):
    try:
        decoded = jwt.decode(token, secret, algorithms = 'HS256')
        return decoded
    except jwt.InvalidTokenError:
        return dic
