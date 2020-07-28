def aceleradev_middleware(get_response):
    def middleware(request):
        if request.method == 'GET':
            print('Metodo da requisição é GET')
        print('================================')
        print('Acelera Dev')
        response = get_response(request)
        print('Online na codenation')
        return response

    return middleware

#Tratamento de erros
#Esperar que o html tenha token
