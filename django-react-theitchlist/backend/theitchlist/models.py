from django.db import models

# Create your models here.
class Theitchlist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
