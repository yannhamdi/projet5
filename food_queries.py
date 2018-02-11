#!/usr/bin/python3
# -*- coding: Utf-8 -*

"Module that manages food"


import records


from database import *



class Food_queries():
    def __init__(self):
        "we initialize our class Food_queries"
        self.info_food = self.db.query("SELECT * FROM food ")   
        



    def query(self, choice_third):
        "query to pick up the food according to the user choice"     
        for self.foods in self.info_food:
            if self.foods.category_id == choice_third:
                print(self.foods.id, self.foods.food_name)



    def better_food(self, food_to_substitute):
        "query to substitute the food choosen"
        self.food_replacing = self.db.query("SELECT * FROM food WHERE category_id =(SELECT category_id FROM food WHERE category_id = {choice}.format(choice =self.second)) AND (SELECT nutrition_grade FROM food WHERE nutrition_grade <(self.foods.nutrition_grade = {substitution}.format(substitution = food_to_substitute))")
        for answer in self.food_replacing:
            print(answer.all())
