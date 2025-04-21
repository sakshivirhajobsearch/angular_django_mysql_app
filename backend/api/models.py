# api/models.py

from django.db import models

class Item(models.Model):
    id = models.BigAutoField(primary_key=True)  # Explicitly set primary key to BigAutoField
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
