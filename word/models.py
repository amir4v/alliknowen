from django.db import models


class Word(models.Model):
    """Word model"""

    word = models.CharField(max_length=100, unique=True)
    iremember = models.BooleanField(default=False)

    def __str__(self):
        return self.word