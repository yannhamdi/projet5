#!/usr/bin/python3
# -*- coding: Utf-8 -*

import records

from database import *

from food_queries import *


class User_choice(Data_base):
    "CLass that interacts with the user"
    def __init__(self):
        Data_base.__init__(self)
        Food_queries.__init__(self)
        " constructor that create the list to double check the user choice"
        self.id_category = []
        self.id_included =[]
        self.id_first_choice = [1,2]
        self.row_category = self.db.query("SELECT id FROM categorie")
        for categ in self.row_category:
            self.id_category.append(categ.id)
        self.row_name = self.db.query("SELECT id FROM food")
        for nam in self.row_name:
            self.id_included.append(nam.id)
    
    def checking_choice(self, choice, liste):
        "function that checks the user choice"
        if choice in liste:
            return True
        else:
            return False

    def first_choice(self):
        "displays the first introdution to the program"
        while True:
            try:
                self.choice = int(input("1 - Sélectionnez un aliment à substituer \n2 - Retrouvez mes aliments substitués"))
                if self.checking_choice(self.choice, self.id_first_choice) == True:
                    break
            except:
                True
        self.second_choice(self.choice)
    def second_choice(self, choice):
        "second degree display choice"
        if choice == 1:
            for r in self.rows:
                print(r.id, r.cat)
        while True:
            try:
                self.second = int(input("Sélectionnez une catégorie"))
                if self.checking_choice(self.second, self.id_category) == True:
                    break
            except:
                True
        self.third_choice(self.second)

    def third_choice(self, third_choice):
        "third degree choice, the user chooses the food to substitute"
        #we call up a method to print out the list of food 
        self.query(third_choice)
        #loop for the user choice until he gives a correct number
        while True:
            # we manage exception in case the user gives a letter for instance
            try:
                self.choice_to_substitute = int(input("Sélectionnez l'aliment à substituer"))
                if self.checking_choice(self.choice_to_substitute, self.id_included) == True:
                    break
            except:
                True
        self.better_food(self.choice_to_substitute)

   


def main():
    user_choice = User_choice()
    user_choice.first_choice()
main()





