from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.


class Sucursal(models.Model):
    name: models.CharField(max_length=30, default="")
    localization: models.CharField(max_length=30, default="")
    responsable: models.OneToOneField(User, null=True, on_delete=CASCADE)
    max_cap: models.IntegerField(default=0)
    entry: models.IntegerField(default=0)
    egress: models.IntegerField(default=0)

    def __str__(self):
        return self.name