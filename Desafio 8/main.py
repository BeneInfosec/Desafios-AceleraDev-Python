
doc = '''
#%RAML 1.0 
title: RAML-api
version: 1.0
mediaType: application/json
protocols: [HTTP,HTTPS]
securitySchemes:
  JWT:
    description: Autenticação por Token JWT
    type: x-JWT
    settings:
      signatures: [HMAC-SHA256]
    describedBy:
      headers:
        Authorization:
            type: string
            required: true
      responses:
        401:
          body:
            application/json:
              type: string
              example: Não autorizado
types:
  Auth:
    type: object
    discriminator: token
    description: Auth Token
    properties:
      token : string
  Mensagem:
    properties:
      mensagem: 
        type: string
  Agent:
    type: object
    discriminator: agent
    description: Agente
    properties:
      agent_id:
        type: integer
      name:
        type: string
      status: 
        type: boolean
      environment:
        type: string
      version:
        type: string
      address:
        type: string
      user_id:
        type: integer
  User:
    type: object
    discriminator: user
    description: Usuário
    properties: 
      user_id:
        type: integer
      name:
        type: string
      password: 
        type: string
      email:
        type: string
      last_login:
        type: date-only
        example: 2015-05-23
  Group:
    type: object
    discriminator: group
    description: Grupo
    properties: 
      group_id:
        type: integer
      name:
        type: string
  Event:
    type: object
    discriminator: event
    description: Evento
    properties: 
      event_id:
        type: integer 
      level:
        type: string
      payload: 
        type: string
      shelve:
        type: boolean
      date:
        type: datetime
      agent_id:
        type: integer
/auth/token:
  post:
    description: Gerador de Token 
    body:             
      application/json:
        username:
          type: string
        password:
          type: string
    responses:
      201:
        body:
          type: Auth
      400:
        body:
          type: Mensagem
          example:
            mensagem: Negado
/agents:
  post: 
    description: Método que inclui um novo agente
    securedBy: [JWT]
    body:             
      type: Agent
    responses:
      201:
        body:
          type: Mensagem
          example:
            mensagem: Operação realizada com sucesso
      400:
        body:
          type: Mensagem
          example:
            mensagem: Agente inválido
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      405:
        body:
          type: Mensagem
          example:
            mensagem: Metodo não permitido
  get: 
    description: Método que lista todos os agentes
    securedBy: [JWT]
    responses:
      200:
        body:
          application/json:
            type: Agent[]
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      500:
        body:
          type: Mensagem
          example:
            mensagem: Ocorreu um erro inesperado
  /{id}:
    get: 
      description: Lista um agente especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            application/json:
              type: Agent[]
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: id não encontrado
    put:
      description: Método que altera um agente especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
    delete: 
      description: Método que exclui um agente especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
  /{id}/events:
    post: 
      description: Método que inclui um novo agente
      securedBy: [JWT]
      body:             
        type: Agent
      responses:
        201:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        400:
          body:
            type: Mensagem
            example:
              mensagem: Agente inválido
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        405:
          body:
            type: Mensagem
            example:
              mensagem: Metodo não permitido
    get: 
      description: Lista um evento especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            application/json:
              type: Event[]
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
    put: 
      description: Método que altera um evento especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
    delete: #Método que exclui um evento relacionado ao cliente
      securedBy: [JWT]
      responses:
          200:
            body:
              type: Mensagem
              example:
                mensagem: Operação realizada com sucesso
          401:
            body:
              type: Mensagem
              example:
                mensagem: Não autorizado 
          404:
            body:
              type: Mensagem
              example:
                mensagem: Não encontrado
/groups:
  post:
    description: Inclui um grupo 
    body:             
      type: Group
    securedBy: [JWT]
    responses:
      201:
        body:
          type: Mensagem
          example:
            mensagem: Operação realizada com sucesso
      400:
        body:
          type: Mensagem
          example:
            mensagem: Agente inválido
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      405:
        body:
          type: Mensagem
          example:
            mensagem: Metodo não permitido
  get:
    description: Lista todos os grupos
    securedBy: [JWT]
    responses:
      200:
        body:
          application/json:
            type: Group[]
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      500:
        body:
          type: Mensagem
          example:
            mensagem: Ocorreu um erro inesperado
  /{id}:
    get: 
      description: Lista um evento especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            application/json:
              type: Group[]
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: id não encontrado
    put: 
      description: Método que altera um evento especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
    delete: 
      description: Método que exclui um evento relacionado ao cliente
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
/users:
  get:
    description: Lista todos os usuários
    securedBy: [JWT]
    responses:
      200:
        body:
          application/json:
            type: User[]
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      500:
        body:
          type: Mensagem
          example:
            mensagem: Ocorreu um erro inesperado
  post:
    description: Inclui usuário
    body:             
      type: Group
    securedBy: [JWT]
    responses:
      201:
        body:
          type: Mensagem
          example:
            mensagem: Operação realizada com sucesso
      400:
        body:
          type: Mensagem
          example:
            mensagem: Agente inválido
      401:
        body:
          type: Mensagem
          example:
            mensagem: Não autorizado
      405:
        body:
          type: Mensagem
          example:
            mensagem: Metodo não permitido
  /{id}:
    get: 
      description: Lista um usuario especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            application/json: 
              type: User[]
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: id não encontrado
    put: 
      description: Método que altera um usuario especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não encontrado
    delete: 
      description: Método que exclui um usuario especifico
      securedBy: [JWT]
      responses:
        200:
          body:
            type: Mensagem
            example:
              mensagem: Operação realizada com sucesso
        401:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
        404:
          body:
            type: Mensagem
            example:
              mensagem: Não autorizado
'''
