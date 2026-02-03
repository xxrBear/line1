from django.db import models

from apps.base.models import BaseModel


class User(BaseModel):
    username = models.CharField(max_length=32, verbose_name='用户名')

    class Meta:
        db_table = 'user'
