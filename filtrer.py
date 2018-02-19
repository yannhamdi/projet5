#!/usr/bin/python3
# -*- coding: Utf-8 -*

"Module that filters the csv file openfood and fill up the databse"


import pandas as pd

import records

from database import *


class DataCreating():
    "class that filters the csv file and only takes what we need"
    def __init__(self):
        "we initialize our file which is going to be usefull for our database"
        self.data_base = Database()
        # I create a list of the columns needed for my database
        self.my_columns = ["code", "url", "product_name", "stores",
                           "nutrition_grade_fr", "main_category_fr"]
        # We open our csv file
        df = pd.read_csv("openfood.csv", sep="\t", low_memory=False)
        self.my_file = (df.loc[(df["countries"] == "France") &
                               (df["main_category_fr"] == "Jus de fruits")
                               | (df["main_category_fr"] == "Charcuteries") |
                               (df["main_category_fr"] == "Snacks sucrés")
                               | (df["main_category_fr"] == "Soupes")
                               | (df["main_category_fr"] == "Fromages") |
                               (df["main_category_fr"] == "Plats préparés")
                               & ((df["nutrition_grade_fr"] == "a")
                                  | (df["nutrition_grade_fr"] == "b")
                                  | (df["nutrition_grade_fr"] == "c")
                                  | (df["nutrition_grade_fr"] == "d")
                                  | (df["nutrition_grade_fr"] == "a")), self.my_columns]).dropna()
        self.my_file.to_csv("myFile.csv", sep="\t")

    def create_data_base(self):
        "we filling up our database"
        id_category = 0
        self.data_base.db.query("DELETE FROM food")
        file_data = pd.read_csv("myFile.csv", sep="\t", low_memory=False)
        for index, row in file_data.iterrows():
            if row["main_category_fr"] == "Jus de fruits":
                id_category = 1
            elif row["main_category_fr"] == "Charcuteries":
                id_category = 2
            elif row["main_category_fr"] == "Snacks sucrés":
                id_category = 3
            elif row["main_category_fr"] == "Soupes":
                id_category = 4
            elif row["main_category_fr"] == "Fromages":
                id_category = 5
            elif row["main_category_fr"] == "Plats préparés":
                id_category = 6
            self.data_base.db.query("""INSERT INTO
                    food(id_openfood, food_link, food_name, store, nutrition_grade , category_id) 
                          VALUES(:id_openfood, :food_link, :food_name, :store, :nutrition_grade, 
                          :category_id)""",
                                    id_openfood=row["code"], food_link=row["url"],
                                    food_name=row["product_name"], store=row["stores"],
                                    nutrition_grade=row["nutrition_grade_fr"], category_id=id_category)


def main():
    "main function that insrances the object of the class Data_Creating"
    data_create = DataCreating()
    data_create.create_data_base()
main()
