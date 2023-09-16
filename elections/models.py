from django.db import models

class Profile(models.Model):
    description = models.TextField(default="description")
