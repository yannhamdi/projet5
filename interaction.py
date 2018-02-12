#!/usr/bin/python3
# -*- coding: Utf-8 -*

import records

from database import *

from food_queries import *

import requests

import json 


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
        self.row_name = self.db.query("SELECT id_openfood FROM food")
        for nam in self.row_name:
            self.id_included.append(nam.id_openfood)

    
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
        if self.choice == 1:
            self.second_choice(self.choice)
        elif self.choice == 2:
            self.search_display()
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
    def third_choice(self, second_choice):
        "third degree choice, the user chooses the food to substitute"
        #we call up a method to print out the list of food 
        self.query(second_choice)
        #loop for the user choice until he gives a correct number
        while True:
            # we manage exception in case the user gives a letter for instance
            try:
                self.choice_to_substitute = int(input("Sélectionnez l'aliment à substituer"))
                if self.checking_choice(self.choice_to_substitute, self.id_included) == True:
                    break
            except:
                True
        self.better_food(self.second, self.choice_to_substitute)

    def substitution_choice(self,listsub):
        "function that allows the user to choose between ten products of substitution"
        while True:
            try:
                self.sub_choice = int(input("Veuillez choisir le produit que vous désirez comme produit de substitution"))
                if self.checking_choice(self.sub_choice, listsub) == True:
                    break
            except:
                True
        self.display_product(self.sub_choice)

    def saving_substitution(self):
        "function that save the user selection"
        while True:
            wishe = input("Souhaitez vous enregistrer votre recherche?")
            if wishe == "oui":
                self.saving_in_database(self.choice_to_substitute, self.sub_choice)
                break
            elif wishe == "non":
                print("Merci!Pour votre recherche")
                break
    
    def deleting_search_data(self):
        "function that allows the user to delete his database search"
        while True:
            del_data = input("Souhaitez vous effacer votre base de données")
            if del_data == "non":
                print("Merci de votre visite")
                break
            elif del_data == "oui":
                self.deleting_data(self)

    
    def display_product(self,code):
        "function that shows the product details"
        api_adress = "https://FR.openfoodfacts.org/api/v0/product/" + str(code) + ".json"
        r=requests.get(api_adress)
        data = r.json()
        print("Nom de l'aliment:", data["product"]["product_name"])
        print("Lieu où l'acheter:",data["product"]["stores"])
        print("Son nutrition grade:", data["product"]["nutrition_grades"])
        print ("Url du produit https://fr.openfoodfacts.org/produit/" + str(code))
        self.saving_substitution()
def main():
    user_choice = User_choice()
    user_choice.first_choice()
main()





