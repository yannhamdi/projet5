#!/usr/bin/python3
# -*- coding: Utf-8 -*

" module that interacts with the user"

import json

import sys

import records

import requests

from food_queries import *



class Userchoice():
    "CLass that interacts with the user"
    def __init__(self):
        " constructor that create the list to double check the user choice"
        # we initialize the class data_base by calling his constructor
        self.data_base = Database()
        # we initialise the class food_queries by calling his constructor
        self.food_queries = Foodqueries()
        # we create list in order tu use them after in our loop for the user interaction
        self.id_category = []
        self.id_included = []
        self.id_first_choice = [1, 2]
        self.row_category = self.data_base.db.query("SELECT id FROM categorie")
        for categ in self.row_category:
            self.id_category.append(categ.id)
        self.row_name = self.data_base.db.query("SELECT id_openfood FROM food")
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
                self.choice = int(input("1 - Sélectionnez un aliment à substituer \n2 - Retrouvez mes aliments substitués "))
                if self.checking_choice(self.choice, self.id_first_choice) is True:
                    break
            except:
                True
        if self.choice == 1:
            self.second_choice(self.choice)
        elif self.choice == 2:
            self.search_display()
    def second_choice(self, choice):
        "second degree display choice"
        # the user choice to find a substitution product
        if choice == 1:
            for r in self.data_base.rows:
                # we print out at the screen the different categories
                print(r.id, r.cat)
        while True:
            try:
                self.second = int(input("Sélectionnez une catégorie "))
                if self.checking_choice(self.second, self.id_category) is True:
                    break
            except:
                True
        self.third_choice(self.second)
    def third_choice(self, second_choice):
        "third degree choice, the user chooses the food to substitute"
        #we call up a method to print out the list of food
        self.food_queries.query(second_choice)
        #loop for the user choice until he gives a correct number
        while True:
            # we manage exception in case the user gives a letter for instance
            try:
                self.choice_to_substitute = int(input("Sélectionnez l'aliment à substituer "))
                if self.checking_choice(self.choice_to_substitute, self.id_included) is True:
                    break
            except:
                True
        self.better_food(self.second, self.choice_to_substitute)


    def better_food(self, choice_category, food_to_substitute):
        "query to substitute the food choosen"
        self.liste_sub = []
        self.food_replacing = self.data_base.db.query("SELECT * FROM food WHERE category_id = {choice} AND nutrition_grade <= (SELECT nutrition_grade FROM food WHERE id_openfood ={grade}) ORDER BY nutrition_grade LIMIT 5".format(choice=choice_category, grade=food_to_substitute))
        for self.answer in self.food_replacing:
            self.liste_sub.append(self.answer.id_openfood)
            print(self.answer.id_openfood, self.answer.food_name, self.answer.nutrition_grade)
        self.substitution_choice(self.liste_sub)

    def substitution_choice(self, listsub):
        "function that allows the user to choose between ten products of substitution"
        while True:
            try:
                self.sub_choice = int(input("Veuillez choisir le produit que vous désirez comme produit de substitution "))
                if self.checking_choice(self.sub_choice, listsub) is True:
                    break
            except:
                True
        self.display_product(self.sub_choice)

    def saving_substitution(self):
        "function that save the user selection"
        while True:
            wishe = input("Souhaitez vous enregistrer votre recherche? ")
            if wishe == "oui":
                self.food_queries.saving_in_database(self.choice_to_substitute, self.sub_choice)
                break
            elif wishe == "non":
                print("Merci!Pour votre recherche")
                break

    def search_display(self):
        "function that displays the user search"
        self.display_search = self.data_base.db.query("SELECT food_substitue.food_name AS to_substitue , User_search.id_to_substitue AS id_substitued ,food_substitued.*, User_search.id_substitued FROM User_search INNER JOIN food AS food_substitue ON food_substitue.id_openfood=User_search.id_to_substitue INNER JOIN food as food_substitued ON food_substitued.id_openfood=User_search.id_substitued")
        for display in self.display_search:
            print(display)
        if len(self.display_search) == 0:
            print("Votre base de données est vide")
            sys.exit()
        else:
            self.deleting_search_data()
            

    def deleting_search_data(self):
        "function that allows the user to delete his database search"
        while True:
            del_data = input("Souhaitez vous effacer votre base de données ")
            if del_data == "non":
                print("Merci de votre visite")
                break
            elif del_data == "oui":
                self.deleting_data()




    def deleting_data(self):
        "function that deletes the database"
        self.deleting = self.data_base.db.query("DELETE FROM User_search")
        print("Votre base de données a été effacée")
        sys.exit()


    def display_product(self, code):
        "function that shows the product details"
        api_adress = "https://FR.openfoodfacts.org/api/v0/product/" + str(code) + ".json"
        r = requests.get(api_adress)
        data = r.json()
        print("Nom de l'aliment:", data["product"]["product_name"])
        print("Lieu où l'acheter:", data["product"]["stores"])
        print("Son nutrition grade:", data["product"]["nutrition_grades"])
        print("Url du produit https://fr.openfoodfacts.org/produit/" + str(code))
        self.saving_substitution()




if __name__ == '__main__':
    main()
