#!/usr/bin/python3
# -*- coding: Utf-8 -*

"module that manages the database"

import records

from food_queries import *



class Data_base():
    def __init__(self):
        "connection to our database openfood"
        self.db = records.Database('mysql+pymysql://root:yh250980@localhost/openfood?charset=utf8mb4')
        self.category_display()



    def category_display(self):
        "function that shows the different category"
        self.rows = self.db.query("SELECT * FROM categorie")

    
            
    

    
         



if __name__ == '__main__':
    main()