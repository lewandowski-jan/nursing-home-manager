# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class Poczty(models.Model):
    kod_poczty = models.CharField(unique=True, max_length=6)
    poczta = models.CharField(max_length=30)

    class Meta:
        db_table = 'poczty'


class Adresy(models.Model):
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=10)
    nr_lokalu = models.CharField(max_length=4, blank=True, null=True)
    poczty = models.ForeignKey(Poczty, on_delete=models.CASCADE)

    class Meta:
        db_table = 'adresy'


class DomySeniora(models.Model):
    nazwa = models.CharField(max_length=50)
    nip = models.CharField(max_length=10)
    krs = models.CharField(max_length=10)
    adresy = models.ForeignKey(Adresy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'domy_seniora'
    
    def __str__(self):
        return "{}-{}".format(self.id, self.nazwa)


class Pokoje(models.Model):
    pietro = models.BigIntegerField()
    pojemnosc = models.BigIntegerField()
    oblozenie = models.BigIntegerField()
    standard = models.CharField(max_length=10)
    czy_przystosowany_do_wozka = models.CharField(max_length=1)

    class Meta:
        db_table = 'pokoje'


class Lozka(models.Model):
    czy_antyodlezynowe = models.CharField(max_length=1)
    dlugosc = models.BigIntegerField()
    opis = models.CharField(max_length=10, blank=True, null=True)
    pokoje = models.ForeignKey(Pokoje, on_delete=models.CASCADE)

    class Meta:
        db_table = 'lozka'
        

class Seniorzy(models.Model):
    pesel = models.CharField(max_length=11, blank=True, null=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    domyseniora = models.ForeignKey(DomySeniora, models.DO_NOTHING)
    lozka = models.ForeignKey(Lozka, on_delete=models.CASCADE)

    class Meta:
        db_table = 'seniorzy'


class RodzajeLekow(models.Model):
    nazwa = models.CharField(unique=True, max_length=30)

    class Meta:
        db_table = 'rodzaje_lekow'


class Leki(models.Model):
    nazwa = models.CharField(max_length=40)
    producent = models.CharField(max_length=100)
    opis = models.CharField(max_length=255, blank=True, null=True)
    ilosc_opakowan = models.BigIntegerField()
    rodzajelekow = models.ForeignKey(RodzajeLekow, models.DO_NOTHING)
    domyseniora = models.ForeignKey(DomySeniora, models.DO_NOTHING)

    class Meta:
        db_table = 'leki'


class KartyZdrowia(models.Model):
    grupa_krwi = models.CharField(max_length=2)
    czynnik_rh = models.CharField(max_length=1)
    uczulenia = models.CharField(max_length=500, blank=True, null=True)
    choroby = models.CharField(max_length=500, blank=True, null=True)
    seniorzy = models.ForeignKey(Seniorzy, on_delete=models.CASCADE)
    leki = models.ManyToManyField(Leki)

    class Meta:
        db_table = 'karty_zdrowia'


class Stanowiska(models.Model):
    nazwa = models.CharField(unique=True, max_length=30)
    opis = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'stanowiska'


class Pracownicy(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    data_zatrudnienia = models.DateField()
    pesel = models.CharField(max_length=11, blank=True, null=True)
    telefon = models.CharField(max_length=11)
    numer_konta = models.CharField(max_length=26, blank=True, null=True)
    adres_email = models.CharField(max_length=100)
    domyseniora = models.ForeignKey(DomySeniora, models.DO_NOTHING)
    adresy = models.ForeignKey(Adresy, models.DO_NOTHING)
    stanowiska = models.ForeignKey(Stanowiska, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pracownicy'


class Wynagrodzenia(models.Model):
    data = models.DateField()
    kwota_podstawowa = models.DecimalField(max_digits=8, decimal_places=2)
    kwota_dodatkowa = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pracownicy = models.ForeignKey(Pracownicy, on_delete=models.CASCADE)

    class Meta:
        db_table = 'wynagrodzenia'