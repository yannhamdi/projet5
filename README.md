# projet5 Application où l'utilisateur peut rechercher un aliment de substitution plus sain
Tout d'abord Installer l'environnement virtuel "pip3 Install virtualenv"
Créer l'environnement virtuel en faisant "virtualenv -p python3 env"
activer l'environnement virtuel "source env/bin/activate"
installer les modules "pip3 install -r requirements.txt"
Ensuite tout d'abord il faut créer la base de données et sa structure pour cela:
Se connecter sur son environnement mysql -u root -p et entrer son mot de passe
Faire CREATE "DATABASE openfood;"
Une fois la base de données créée: USE openfood;
Puis SOURCE chemindufichier/structure.sql;
Télécharger le fichier csv http://fr.openfoodfacts.org/data/fr.openfoodfacts.org.products.csv
Puis pour remplir notre base de données faire python3 filtrer.py
