from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=32, unique=True)
    body = models.TextField()

    def __str__(self):
        return f"Title: {self.title}"