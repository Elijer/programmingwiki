from django.db import models

class Entry(models.Model):
    ref = models.CharField(max_length=50, null=False, unique=True, primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()

    #def save(self, *args, **kwargs):
    #    self.ref = self.title.lower()
    #    super(Entry, self).save(*args, **kwargs)

    def __str__(self):
        return f"Title: {self.title}"