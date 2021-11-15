from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    pages = models.IntegerField()

    def __repr__(self):
        return f"ID: {self.id} - Title: {self.title}"
