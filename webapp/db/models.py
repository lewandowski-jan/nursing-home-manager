# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adresy(models.Model):
    id_adresu = models.BigIntegerField(primary_key=True)
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_budynku = models.CharField(max_length=10)
    nr_lokalu = models.CharField(max_length=4, blank=True, null=True)
    id_poczty = models.ForeignKey('Poczty', models.DO_NOTHING, db_column='id_poczty')

    class Meta:
        managed = False
        db_table = 'adresy'


class DomySeniora(models.Model):
    id_domu_seniora = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    nip = models.CharField(max_length=10)
    krs = models.CharField(max_length=10)
    id_adresu = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'domy_seniora'


class KartyZdrowia(models.Model):
    id_karty = models.BigIntegerField(primary_key=True)
    grupa_krwi = models.CharField(max_length=2)
    czynnik_rh = models.CharField(max_length=1)
    uczulenia = models.CharField(max_length=500, blank=True, null=True)
    choroby = models.CharField(max_length=500, blank=True, null=True)
    id_seniora = models.ForeignKey('Seniorzy', models.DO_NOTHING, db_column='id_seniora')

    class Meta:
        managed = False
        db_table = 'karty_zdrowia'


class KategoriePrawaJazdy(models.Model):
    id_kategorii = models.BigIntegerField(primary_key=True)
    kod_kategorii = models.CharField(unique=True, max_length=4)
    opis = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kategorie_prawa_jazdy'


class Leki(models.Model):
    id_leku = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(max_length=40)
    producent = models.CharField(max_length=100)
    opis = models.CharField(max_length=255, blank=True, null=True)
    ilosc_opakowan = models.BigIntegerField()
    id_rodzaju = models.ForeignKey('RodzajeLekow', models.DO_NOTHING, db_column='id_rodzaju')
    id_domu_seniora = models.ForeignKey(DomySeniora, models.DO_NOTHING, db_column='id_domu_seniora')

    class Meta:
        managed = False
        db_table = 'leki'


class Lozka(models.Model):
    id_lozka = models.BigIntegerField(primary_key=True)
    czy_antyodlezynowe = models.CharField(max_length=1)
    dlugosc = models.BigIntegerField()
    opis = models.CharField(max_length=10, blank=True, null=True)
    id_pokoju = models.ForeignKey('Pokoje', models.DO_NOTHING, db_column='id_pokoju')

    class Meta:
        managed = False
        db_table = 'lozka'


class Marki(models.Model):
    id_marki = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'marki'


class Modele(models.Model):
    id_modelu = models.BigIntegerField(primary_key=True, null=False)
    nazwa = models.OneToOneField(Marki, models.DO_NOTHING, db_column='nazwa')

    class Meta:
        managed = False
        db_table = 'modele'


class OsobaKontaktowaSenior(models.Model):
    id_osobakontaktowaseniora = models.BigIntegerField(primary_key=True)
    id_osoby = models.BigIntegerField()
    id_seniora = models.BigIntegerField()

    class Meta:
        db_table = 'osoba_kontaktowa_senior'


class OsobyKontaktowe(models.Model):
    id_osoby = models.BigIntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    telefon = models.CharField(max_length=11)
    adres_email = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'osoby_kontaktowe'


class Poczty(models.Model):
    id_poczty = models.BigIntegerField(primary_key=True)
    kod_poczty = models.CharField(unique=True, max_length=6)
    poczta = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'poczty'


class Pojazdy(models.Model):
    id_pojazdu = models.BigIntegerField(primary_key=True)
    numer_rejestracyjny = models.CharField(max_length=7)
    pojemnosc = models.BigIntegerField()
    czy_przystosowany_do_wozka = models.CharField(max_length=1)
    przebieg = models.BigIntegerField()
    data_nastepnego_przegladu = models.DateField()
    opis_stanu = models.CharField(max_length=500)
    id_pracownika = models.ForeignKey('Pracownicy', models.DO_NOTHING, db_column='id_pracownika', blank=True, null=True)
    id_domu_seniora = models.ForeignKey(DomySeniora, models.DO_NOTHING, db_column='id_domu_seniora')
    id_modelu = models.ForeignKey(Modele, models.DO_NOTHING, db_column='id_modelu')

    class Meta:
        managed = False
        db_table = 'pojazdy'


class Pokoje(models.Model):
    id_pokoju = models.BigIntegerField(primary_key=True)
    pietro = models.BigIntegerField()
    pojemnosc = models.BigIntegerField()
    oblozenie = models.BigIntegerField()
    standard = models.CharField(max_length=10)
    czy_przystosowany_do_wozka = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pokoje'


class Pracownicy(models.Model):
    id_pracownika = models.BigIntegerField(primary_key=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    data_zatrudnienia = models.DateField()
    pesel = models.CharField(max_length=11, blank=True, null=True)
    telefon = models.CharField(max_length=11)
    numer_konta = models.CharField(max_length=26, blank=True, null=True)
    adres_email = models.CharField(max_length=100)
    id_domu_seniora = models.ForeignKey(DomySeniora, models.DO_NOTHING, db_column='id_domu_seniora')
    id_adresu = models.ForeignKey(Adresy, models.DO_NOTHING, db_column='id_adresu')
    id_stanowiska = models.ForeignKey('Stanowiska', models.DO_NOTHING, db_column='id_stanowiska')

    class Meta:
        managed = False
        db_table = 'pracownicy'


class PracownicyKategorie(models.Model):
    id_pracownicykategorie = models.BigIntegerField(primary_key=True)
    id_pracownika = models.OneToOneField(Pracownicy, models.DO_NOTHING, db_column='id_pracownika', primary_key=True)
    id_kategorii = models.ForeignKey(KategoriePrawaJazdy, models.DO_NOTHING, db_column='id_kategorii')

    class Meta:
        db_table = 'pracownicy_kategorie'
        unique_together = (('id_pracownika', 'id_kategorii'),)


class PrzyjmowaneLeki(models.Model):
    id_leku = models.BigIntegerField()
    id_karty = models.ForeignKey(KartyZdrowia, models.DO_NOTHING, db_column='id_karty')
    data_od = models.DateField()
    data_do = models.DateField()
    dawka = models.CharField(max_length=100)
    czestotliwosc = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'przyjmowane_leki'


class RodzajeLekow(models.Model):
    id_rodzaju = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'rodzaje_lekow'


class Seniorzy(models.Model):
    id_seniora = models.BigIntegerField(primary_key=True)
    pesel = models.CharField(max_length=11, blank=True, null=True)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    zdjecie = models.BinaryField(blank=True, null=True)
    id_domu_seniora = models.ForeignKey(DomySeniora, models.DO_NOTHING, db_column='id_domu_seniora')
    id_lozka = models.ForeignKey(Lozka, models.DO_NOTHING, db_column='id_lozka')

    class Meta:
        managed = False
        db_table = 'seniorzy'


class SqlplusData(models.Model):
    product = models.CharField(max_length=30)
    userid = models.CharField(max_length=128, blank=True, null=True)
    attribute = models.CharField(max_length=240, blank=True, null=True)
    scope = models.CharField(max_length=240, blank=True, null=True)
    numeric_value = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    char_value = models.CharField(max_length=240, blank=True, null=True)
    date_value = models.DateField(blank=True, null=True)
    long_value = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlplus_data'


class Stanowiska(models.Model):
    id_stanowiska = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(unique=True, max_length=30)
    opis = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stanowiska'


class Wplaty(models.Model):
    id_wplaty = models.BigIntegerField(primary_key=True)
    data = models.DateField()
    kwota = models.DecimalField(max_digits=10, decimal_places=2)
    rodzaj = models.CharField(max_length=1)
    konto_nadawcy = models.CharField(max_length=26, blank=True, null=True)
    id_seniora = models.ForeignKey(Seniorzy, models.DO_NOTHING, db_column='id_seniora')

    class Meta:
        managed = False
        db_table = 'wplaty'


class Wynagrodzenia(models.Model):
    id_wynagrodzenia = models.BigIntegerField(primary_key=True)
    data = models.DateField()
    kwota_podstawowa = models.DecimalField(max_digits=8, decimal_places=2)
    kwota_dodatkowa = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    id_pracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='id_pracownika')

    class Meta:
        managed = False
        db_table = 'wynagrodzenia'


class Wyposazenie(models.Model):
    id_wyposazenia = models.BigIntegerField(primary_key=True)
    nazwa = models.CharField(max_length=50)
    ilosc = models.BigIntegerField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    opis = models.CharField(max_length=200, blank=True, null=True)
    id_pracownika = models.ForeignKey(Pracownicy, models.DO_NOTHING, db_column='id_pracownika', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wyposazenie'


class WyposazeniePokoj(models.Model):
    id_wyposazenia = models.ForeignKey(Wyposazenie, models.DO_NOTHING, db_column='id_wyposazenia')
    id_pokoju = models.ForeignKey(Pokoje, models.DO_NOTHING, db_column='id_pokoju')

    class Meta:
        managed = False
        db_table = 'wyposazenie_pokoj'