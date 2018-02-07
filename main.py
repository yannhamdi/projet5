#!/usr/bin/python3
# -*- coding: Utf-8 -*
from filtrer import *

import records




def main():
    data_create = Data_Creating()
    data_create.create_data_base()
    #we ask the user to choose what he wants to do
    choice = input("1-Quels aliments souhaitez-vous remplacer\n2- Retrouver vos aliments substitués")
    int(choice)
    db = records.Database('mysql+pymysql://root:yh250980@localhost/openfood?charset=utf8mb4')
    if choice == 1:
        rows = db.query("SELECT * FROM categorie")
        for r in rows:
            print(r.id, r.cat)
main()

