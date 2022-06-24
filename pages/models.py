from django.db import models

# Create your models here.
class OsauhinguAndmedModel(models.Model):
    nimi = models.TextField(max_length=100)
    registrikood = models.CharField(max_length=7)

    def __str__(self) -> str:
        return self.nimi + ": " + str(self.registrikood)
