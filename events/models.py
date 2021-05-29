from django.db import models
from graphql.type.definition import T

class Event(models.Model):
    name = models.TextField()
    url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name