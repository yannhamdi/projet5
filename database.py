#!/usr/bin/python3
# -*- coding: Utf-8 -*

"module that manages the database"

import records

from food_queries import *



class Data_base(Food_queries):
    def __init__(self):
        "connection to our database openfood"
        self.db = records.Database('mysql+pymysql://root:yh250980@localhost/openfood?charset=utf8mb4')
        self.category_display()



    def category_display(self):
        "function that shows the different category"
        self.rows = self.db.query("SELECT * FROM categorie")

    def search_display(self):
        "function that displays the user search"
        self.display_search = self.db.query("SELECT food_substitue.food_name AS to_substitue , User_search.id_to_substitue AS id_substitued ,food_substitued.*, User_search.id_substitued FROM User_search INNER JOIN food AS food_substitue ON food_substitue.id_openfood=User_search.id_to_substitue INNER JOIN food as food_substitued ON food_substitued.id_openfood=User_search.id_substitued")
        for display in self.display_search:
            print(display)
        self.deleting_search_data()
            


    def deleting_data(self):
        "function that deletes the database"
        self.deleting = self.db.query("DELETE FROM User_search")
        print("Votre base de données a été effacée")
         
