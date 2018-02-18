#!/usr/bin/python3
# -*- coding: Utf-8 -*

"Module that manages food"


from database import *

from interaction import *



class Food_queries():
    "class that manages queries of products"
    def __init__(self):
        "we initialize our class Food_queries"
        self.data_base = Data_base()
        self.info_food = self.data_base.db.query("SELECT * FROM food")


    def query(self, second_choice):
        "query to pick up products according to the user choice"
        for self.foods in self.info_food:
            if self.foods.category_id == second_choice:
                print(self.foods.id_openfood, self.foods.food_name, self.foods.nutrition_grade)



    


    def saving_in_database(self, choice_to_substitute, sub_choice):
        "function that save the user search in database"
        self.saving = self.data_base.db.query("INSERT INTO User_search(id_to_substitue, id_substitued) VALUES(:id_to_substitue, :id_substitued)", id_to_substitue=choice_to_substitute, id_substitued=sub_choice)



if __name__ == '__main__':
    main()