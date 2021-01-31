from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField('name', max_length=60)
    emp_id=models.IntegerField(default='0')
    email_id=models.CharField('email', max_length=60, default='email@g.com')


    object = models.Manager()