# projet5 Application où l'utilisateur peut rechercher un aliment de substitution plus sain

1-Tout d'abord Installer l'environnement virtuel "pip3 Install virtualenv"

2-Créer l'environnement virtuel en faisant "virtualenv -p python3 env"

3-Activer l'environnement virtuel "source env/bin/activate"
4-installer les modules "pip3 install -r requirements.txt"

5-Ensuite tout d'abord il faut créer la base de données et sa structure pour cela:

6-Se connecter sur son environnement mysql -u root -p et entrer son mot de passe

7-Faire CREATE "DATABASE openfood;"

8-Une fois la base de données créée: USE openfood;

9-Puis SOURCE chemindufichier/structure.sql;

10-Télécharger le fichier csv http://fr.openfoodfacts.org/data/fr.openfoodfacts.org.products.csv

11-Puis pour remplir notre base de données faire python3 filtrer.py

12-Puis lancer l'application python3 main.py