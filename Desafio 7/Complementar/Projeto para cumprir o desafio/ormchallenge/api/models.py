from django.core.validators import MinLengthValidator, EmailValidator, validate_ipv4_address
from django.db import models
import datetime

# Create your models here.
LEVEL_CHOICES = [
    ('critical', 'critical.'),
    ('debug', 'debug'),
    ('error', 'error'),
    ('warning', 'warning'),
    ('information', 'info'),
]

min_validator = MinLengthValidator(8, 'the password cant be small then 8')


class Group(models.Model):
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(validators=[EmailValidator], null=True)
    password = models.CharField(max_length=50, validators=[min_validator])
    last_login = models.DateField(default=datetime.date.today)
    group = models.ManyToManyField(Group)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Agent(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    address = models.GenericIPAddressField(validators=[validate_ipv4_address], null=True)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    data = models.TextField(max_length=500)
    agent = models.OneToOneField(Agent, on_delete=models.PROTECT)
    arquivado = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.level +' in ' + self.agent.name

    class Meta:
        ordering = ['date']

