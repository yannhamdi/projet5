#!/usr/bin/python3
# -*- coding: Utf-8 -*

"module that manages the database"

from settings import *

import records

from food_queries import *


class Database():
    "class that connects to the database mysql"
    def __init__(self):
        "connection to our database openfood"
        data_code = ("mysql+pymysql://" + str(login)+ ":" + str(password) + "@localhost/openfood?charset=utf8mb4")
        self.db = records.Database(data_code)
        self.category_display()



    def category_display(self):
        "function that shows the different category"
        self.rows = self.db.query("SELECT * FROM categorie")



if __name__ == '__main__':
    main()
