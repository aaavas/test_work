from datetime import date
from tkinter import CASCADE
from wsgiref import validate
from django.db import models
from django.forms import ValidationError
import re, django
from django_project import settings

# Create your models here.


class OsanikModel(models.Model):
    nimi = models.TextField(null=False)
    kood = models.CharField(max_length=11)

    def __str__(self):
        return self.nimi + " - " + str(self.kood)


class OsauhinguAndmedModel(models.Model):
    def validate_nimi(name):
        if len(name) < 3 or len(name) > 100:
            raise ValidationError("Nimi peab olema 3 kuni 100 tähte või numbrit pikk")

    def validate_registrikood(kood):
        if len(kood) != 7 and not re.match(r"^([\d]+)$", kood):
            raise ValidationError("Registrikood peab olema 7 numbrit pikk")

    def validate_asutamiskp(kp):
        if kp > date.today():
            raise ValidationError(
                "Asutamiskuupäev peab olema väiksem või võrdne tänasega"
            )

    def validate_kapital(kapital):
        if not re.match(r"^([\d]+)$", str(kapital)) and int(kapital) < 2500:
            raise ValidationError(
                "Kogukapital peab olema summa eurodes ja mitte väiksem kui 2500"
            )

    nimi = models.TextField(null=False, blank=False, validators=[validate_nimi])
    registrikood = models.CharField(
        null=False,
        blank=False,
        unique=True,
        max_length=7,
        validators=[validate_registrikood],
    )
    asutamiskp = models.DateField(
        blank=False,
        validators=[validate_asutamiskp],
    )
    kapital = models.PositiveIntegerField(
        null=False, blank=False, default=5000, validators=[validate_kapital]
    )
    osanikud = models.ManyToManyField(OsanikModel, through="Osalus")

    def __str__(self) -> str:
        return self.nimi + ": " + str(self.registrikood)


class Osalus(models.Model):
    def validate_osaluse_suurus(osaluse_suurus):
        if osaluse_suurus < 1:
            raise ValidationError("Osaluse suurus peab olema suurem või võrdne 1ga")

    person = models.ForeignKey(OsanikModel, on_delete=models.CASCADE)
    company = models.ForeignKey(OsauhinguAndmedModel, on_delete=models.CASCADE)
    osaluse_suurus = models.PositiveIntegerField(validators=[validate_osaluse_suurus])
    asutaja = models.BooleanField(default=False)
