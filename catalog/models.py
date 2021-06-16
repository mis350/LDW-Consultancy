from django.db import models

# Create your models here.
class Book(models.Model):
  title = models.CharField(max_length=200)
  author = models.ForeignKey('Author', null=True)
  summary = models.TextField(max_length=1000)
  isbn = models.CharField('ISBN', max_length=13, unique=True,

