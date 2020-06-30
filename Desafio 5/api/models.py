from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator

class User(models.Model):
    name = models.CharField('Nome', max_length = 50)
    #Implementação do last_login
    last_login = models.DateTimeField('Last Login', auto_now=True)
    #Implementação da validação de email
    email = models.CharField('email', max_length = 254, validators =[EmailValidator()])
    #Implementar validação de password
    password = models.CharField('password', max_length = 50, validators=[MinLengthValidator(8)])

    def __str__(self): #Converter para string
        return self.name


class Agent(models.Model):
    name = models.CharField('Nome', max_length = 50)
    status = models.BooleanField(default = False)
    env = models.CharField('Env', max_length = 20)
    version = models.CharField('Version', max_length = 5)
    address = models.GenericIPAddressField('Endereço IPv4',max_length = 39, protocol = 'IPv4')

    def __str__(self): #Converter para string
        return self.name


class Event(models.Model):
    level = models.CharField(['CRITICAL','DEBUG','ERROR','INFO' ], max_length = 20)
    data = models.TextField('data', max_length = 20)
    arquivado = models.BooleanField(default = False)
    date = models.DateField('Data', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self): #Converter para string
        return self.name


class Group(models.Model):
    name = models.CharField('Nome', max_length = 50)

    def __str__(self): #Converter para string
        return self.name

class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
