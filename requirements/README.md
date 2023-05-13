# Vérification de la cohérence des versions des modules avec `pip`

Pour vérifier la cohérence entre les versions des modules répertoriés dans un fichier `requirements.txt` et les versions réellement installées, vous pouvez utiliser la commande `pip check`. Cette commande permet de détecter les incompatibilités entre les versions des modules et les dépendances spécifiées dans le fichier `requirements.txt`.

Voici les étapes à suivre pour vérifier la cohérence des versions des modules :

1. Assurez-vous que vous avez `pip` installé et accessible depuis votre ligne de commande.

2. Ouvrez une ligne de commande et placez-vous dans le répertoire contenant le fichier `requirements.txt`.

3. Exécutez la commande suivante :

```shell
pip check -r requirements_prod.txt
