from django.db import models

# Create your models here.


class Lambda(models.Model):
    question = models.CharField('question', max_length=40)
