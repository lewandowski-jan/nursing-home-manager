# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.db.models.fields import NullBooleanField


class Poczty(models.Model):
    kod_poczty = models.CharField(unique=True, max_length=6)
    poczta = models.CharField(max_length=30)

    class Meta:
        db_table = 'poczty'
        verbose_name_plural = 'poczty'

    def __str__(self):
        return f'{self.id}: {self.kod_poczty} {self.poczta}'


class Adresy(models.Model):
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=10)
    nr_lokalu = models.CharField(max_length=4, blank=True, null=True)
    poczty = models.ForeignKey(Poczty, on_delete=models.PROTECT)

    class Meta:
        db_table = 'adresy'
        verbose_name_plural = 'adresy'

    def __str__(self):
        s = f'{self.id}: {self.miasto} ul. {self.ulica} {self.nr_budynku}'
        if self.nr_lokalu is not None:
            s += f'/{self.nr_lokalu}'
        return s


class DomySeniora(models.Model):
    nazwa = models.CharField(max_length=50)
    nip = models.CharField(max_length=10)
    krs = models.CharField(max_length=10)
    adresy = models.OneToOneField(Adresy, on_delete=models.PROTECT)

    class Meta:
        db_table = 'domy_seniora'
        verbose_name_plural = 'domy_seniora'
    
    def __str__(self):
        return f'{self.id}: {self.nazwa}'


class Pokoje(models.Model):
    pietro = models.BigIntegerField()
    pojemnosc = models.BigIntegerField()
    oblozenie = models.BigIntegerField()
    standard = models.CharField(max_length=10)
    czy_przystosowany_do_wozka = models.CharField(max_length=1)

    class Meta:
        db_table = 'pokoje'
        verbose_name_plural = 'pokoje'

    def __str__(self):
        return f'{self.id}: Poziom {self.pietro}, Oblozenie: {self.oblozenie}/{self.pojemnosc} Standard: {self.standard}, Wózek:{self.czy_przystosowany_do_wozka}'
        


class Lozka(models.Model):
    czy_antyodlezynowe = models.CharField(max_length=1)
    dlugosc = models.BigIntegerField()
    opis = models.CharField(max_length=10, blank=True, null=True)
    pokoje = models.ForeignKey(Pokoje, on_delete=models.PROTECT)

    class Meta:
        db_table = 'lozka'
        verbose_name_plural = 'lozka'
    
    def __str__(self):
        s = f'{self.id}: Dł. ={self.dlugosc}cm, Antyodlezynowe: {self.czy_antyodlezynowe}'
        if self.opis is not None:
            s += f', {self.opis}'
        return s 
        

class Seniorzy(models.Model):
    pesel = models.CharField(max_length=11, blank=True, null=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    domyseniora = models.ForeignKey(DomySeniora, models.PROTECT)
    lozka = models.OneToOneField(Lozka, on_delete=models.PROTECT)

    class Meta:
        db_table = 'seniorzy'
        verbose_name_plural = 'seniorzy'

    def __str__(self):
        return f'{self.id}: {self.imie} {self.nazwisko}  PESEL: {self.pesel}'


class RodzajeLekow(models.Model):
    nazwa = models.CharField(unique=True, max_length=30)

    class Meta:
        db_table = 'rodzaje_lekow'
        verbose_name_plural = 'rodzaje_lekow'

    def __str__(self):
        return f'{self.id}: {self.nazwa}'


class Leki(models.Model):
    nazwa = models.CharField(max_length=40)
    producent = models.CharField(max_length=100)
    opis = models.CharField(max_length=255, blank=True, null=True)
    ilosc_opakowan = models.BigIntegerField()
    rodzajelekow = models.ForeignKey(RodzajeLekow, models.PROTECT)
    domyseniora = models.ForeignKey(DomySeniora, models.PROTECT)

    class Meta:
        db_table = 'leki'
        verbose_name_plural = 'leki'

    def __str__(self):
        return f'{self.id}: {self.nazwa}: {self.ilosc_opakowan} szt.'


class KartyZdrowia(models.Model):
    grupa_krwi = models.CharField(max_length=2)
    czynnik_rh = models.CharField(max_length=1)
    uczulenia = models.CharField(max_length=500, blank=True, null=True)
    choroby = models.CharField(max_length=500, blank=True, null=True)
    seniorzy = models.OneToOneField(Seniorzy, on_delete=models.PROTECT)
    leki = models.ManyToManyField(Leki, blank=True)

    class Meta:
        db_table = 'karty_zdrowia'
        verbose_name_plural = 'karty_zdrowia'

    def __str__(self):
        return f'{self.id}: {self.seniorzy.imie} {self.seniorzy.nazwisko}'


class Stanowiska(models.Model):
    nazwa = models.CharField(unique=True, max_length=30)
    opis = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'stanowiska'
        verbose_name_plural = 'stanowiska'

    def __str__(self):
        return f'{self.id}: {self.nazwa}'


class Pracownicy(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    data_zatrudnienia = models.DateField()
    pesel = models.CharField(max_length=11, blank=True, null=True)
    telefon = models.CharField(max_length=11)
    numer_konta = models.CharField(max_length=26, blank=True, null=True)
    adres_email = models.CharField(max_length=100)
    domyseniora = models.ForeignKey(DomySeniora, models.PROTECT)
    adresy = models.ForeignKey(Adresy, models.PROTECT)
    stanowiska = models.ForeignKey(Stanowiska, on_delete=models.PROTECT)

    class Meta:
        db_table = 'pracownicy'
        verbose_name_plural = 'pracownicy'

    def __str__(self):
        return f'{self.id}: {self.imie} {self.nazwisko}, {self.stanowiska.nazwa}'


class Wynagrodzenia(models.Model):
    data = models.DateField()
    kwota_podstawowa = models.DecimalField(max_digits=8, decimal_places=2)
    kwota_dodatkowa = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pracownicy = models.ForeignKey(Pracownicy, on_delete=models.PROTECT)

    class Meta:
        db_table = 'wynagrodzenia'
        verbose_name_plural = 'wynagrodzenia'

    def __str__(self):
        return f'{self.id}: {self.pracownicy.imie} {self.pracownicy.nazwisko}, {self.kwota_podstawowa} + {self.kwota_dodatkowa}'