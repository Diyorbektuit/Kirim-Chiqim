from django.db import models


class TgUsers(models.Model):
    username = models.CharField(max_length=123)
    first_name = models.CharField(max_length=123)
    last_name = models.CharField(max_length=123)
    tg_id = models.PositiveIntegerField()

    def __str__(self):
        return self.username

