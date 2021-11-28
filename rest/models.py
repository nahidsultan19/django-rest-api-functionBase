from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    age = models.TextField()


    def __str__(self):
        return self.name
