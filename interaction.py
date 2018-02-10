#!/usr/bin/python3
# -*- coding: Utf-8 -*

import records

from database import *


class User_choice(Data_base):
    "CLass that interacts with the user"
    def __init__(self):
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
            return 1
        else:
            return 0

    def first_choice(self):
        "displays the first introdution to the program"
        while True:
            try:
                self.choice = int(input("alors"))
                if self.checking_choice(self.choice, self.id_first_choice) == 1:
                    break
            except:
                True
        self.second_choice(self.choice)
    def second_choice(self, choice):
        "second degree display choice"
        if choice == 1:
            for r in Data_base.rows:
                print(r.id, r.cat)

            	

   


def main():
    user_choice = User_choice()
    user_choice.first_choice()
main()





