from django.db import models


class User(models.Model):
    username = models.CharField(max_length=32, verbose_name='用户名')

    class Meta:
        db_table = 'user'
