# TP1 - Web Scraping avec Playwright

Ce projet de web scraping utilise Playwright pour extraire des données de sites web. Il permet de naviguer sur des pages web, d'extraire des informations structurées et de les sauvegarder dans un fichier CSV.

## Structure du Projet

tp1/
├── scraping/
├── navigation.py # Gestion de la navigation entre les pages │
├── config.py # Configuration des sélecteurs et paramètres │
├── extract.py # Extraction des données des pages │
├── save.py # Sauvegarde des données dans un fichier CSV
├── main.py # Script principal
├── requirements.txt # Dépendances Python nécessaires
├── README.md # Documentation du projet

## Fonctionnalités

- **Navigation** : Utilisation de Playwright pour naviguer sur les pages web.
- **Gestion des cookies** : Fermeture automatique des bannières de cookies.
- **Pagination** : Navigation automatique entre les pages.
- **Extraction** : Récupération des données structurées (titres, prix, liens, etc.).
- **Sauvegarde** : Export des données extraites dans un fichier CSV.

## Prérequis

1. **Python 3.9+** : Assurez-vous que Python est installé sur votre machine.
2. **Dépendances** : Installez les dépendances listées dans `requirements.txt` :

   ```bash
   pip install -r requirements.txt
   ```

   Playwright : Installez les navigateurs nécessaires pour Playwright

   ```bash
   playwright install
   ```

## Utilisation

Clonez ce dépôt sur votre machine locale : https://github.com/douniaboujnane/webScraping

Lancez le script principal : main.py

Les données extraites seront sauvegardées dans un fichier CSV.

## Configuration

Les paramètres principaux (URL cible, sélecteurs CSS, etc.) sont définis dans le fichier config.py. Vous pouvez modifier ce fichier pour adapter le script à d'autres sites web.

## Dépendances

Playwright
Pandas

# Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser et de le modifier.
