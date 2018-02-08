#!/usr/bin/python3
# -*- coding: Utf-8 -*


import records


class User_choice:
    "CLass that interacts with the user"
    def __init__(self):
        self.db = records.Database('mysql+pymysql://root:yh250980@localhost/openfood?charset=utf8mb4')
        #we ask the user to choose what he wants to do
        self.choice = input("1-Quels aliments souhaitez-vous remplacer\n2- Retrouver vos aliments substitués")
        self.choice = int(self.choice)
        # while the user choice is not 1 or 2 we reiterate the question
        if self.choice == 1: 
            rows = self.db.query("SELECT * FROM categorie")
            for r in rows:
                print(r.id, r.cat)
            self.choice_category = input("Sélectionnez la catégorie")
            self.choice_category = int(self.choice_category)
            self.display_food_name()
        else:
            while self.choice != 2:
                self.choice = input("1-Quels aliments souhaitez-vous remplacer\n2- Retrouver vos aliments substitués")
    



    
    def display_food_name(self):
        "function that displays the product by category"
        id_included = []
        rows_food = self.db.query("SELECT id, food_name FROM food WHERE category_id ={choice}".format(choice = self.choice_category))
        for product in rows_food:
            print(product.id, product.food_name)
            id_included.append(product.id)
        choice_food = input ("Sélectionnez numéro de l'aliment à substituer")
        choice_food = int(choice_food)
        if choice_food in id_included:
            print("ok")
        else:
            while choice_food not in id_included:
                choice_food = input("Sélectionnez numéro de l'aliment à substituer") 
                choice_food = int(choice_food)
                if choice_food in id_included:
                    break

def main():
    user_choice = User_choice()
main()



