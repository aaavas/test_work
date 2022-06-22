from django.db import models

# Create your models here.
class OsauhinguAndmed(models.Model):
    nimi = models.TextField()
    registrikood = models.IntegerField()

    def __str__(self) -> str:
        return self.nimi
