from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=32, unique=True)
    content = models.TextField()

    def __str__(self):
        return f"Title: {self.title}"