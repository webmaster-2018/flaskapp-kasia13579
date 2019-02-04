#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  modele.py

from peewee import *

baza_plik = 'quiz.db'
baza = SqliteDatabase(baza_plik)  # instancja bazy

### MODELE #
class BazaModel(Model):
    class Meta:
        database = baza


class Uczen(BazaModel):
    pass


class Klasa(BazaModel):
    pass


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
