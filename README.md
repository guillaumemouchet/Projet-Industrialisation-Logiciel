# projet-indu-log

Ce projet a été réalisé durant le cours d'Industrialisation du Logiciel. Il a pour but de mettre en pratique des éléments d'intégrations continus. Nous avons décidé de créer un générateur de mots-de-passe grâce à Flask.

# WARNING : TODO BEFORE PUSH

Don't forget the change the version in the setup.py. The creation of the wheel won't work if the versions are the same.

# Comment lancer le projet

1. Mettre en place un environnement virtuel si pas déjà fait : `$ python -m venv venv`
2. Activer le venv : `$ source venv/bin/activate`
3. Installer les requirements : `pip install -r requirements.txt`
4. Lancer l'app : `$ FLASK_APP="main.py" flask run --debug` (pour le logger, spécifier le port avant avec `export FLASK_RUN_PORT=8000` et remplacer `main.py` par `logger.py`)
5. Pour windows : `flask --app main.py run` (pour le logger `$env:FLASK_RUN_PORT=8000`)
