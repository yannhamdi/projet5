#!/usr/bin/python3
# -*- coding: Utf-8 -*

"Module that manages food"


from database import *


class Food_queries():
    "class that manages queries of products"
    def __init__(self):
        "we initialize our class Food_queries"
        self.info_food = self.db.query("SELECT * FROM food")


    def query(self, second_choice):
        "query to pick up products according to the user choice"
        for self.foods in self.info_food:
            if self.foods.category_id == second_choice:
                print(self.foods.id_openfood, self.foods.food_name)



    def better_food(self, choice_category, food_to_substitute):
        "query to substitute the food choosen"
        self.liste_sub = []
        self.food_replacing = self.db.query("SELECT * FROM food WHERE category_id = {choice} AND nutrition_grade <= (SELECT nutrition_grade FROM food WHERE id_openfood ={grade}) ORDER BY nutrition_grade LIMIT 5".format(choice=choice_category, grade=food_to_substitute))
        for self.answer in self.food_replacing:
            self.liste_sub.append(self.answer.id_openfood)
            print(self.answer.id_openfood, self.answer.food_name, self.answer.nutrition_grade)
        self.substitution_choice(self.liste_sub)


    def saving_in_database(self, choice_to_substitute, sub_choice):
        "function that save the user search in database"
        self.saving = self.db.query("INSERT INTO User_search(id_to_substitue, id_substitued) VALUES(:id_to_substitue, :id_substitued)", id_to_substitue=choice_to_substitute, id_substitued=sub_choice)
