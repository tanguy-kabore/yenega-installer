# yenega-installer

## Introduction

Bienvenue dans le projet Yenega ! Ce projet utilise un installateur Python pour simplifier le processus de création d'un nouveau projet basé sur le framework Yenega.

## Prérequis

Assurez-vous que les éléments suivants sont installés sur votre système avant d'utiliser l'installateur Yenega :

- Python: [Installer Python 3](https://www.python.org/downloads)
- Git: [Installer Git](https://git-scm.com/downloads)

## Utilisation de l'Installateur

### 1. Cloner le Projet Yenega

```bash
git clone https://gitlab.com/yenega/yenega-installer.git
```

### 2. Exécution de l'Installateur

Utilisez le script [yenega-installer.py](https://gitlab.com/yenega/yenega-installer.git) pour créer un nouveau projet Yenega. Assurez-vous d'être dans le répertoire où vous souhaitez créer votre projet.

```bash
python path/vers/yenega-installer.py new NomDuProjet
```
Remplacez **path/vers/yenega-installer.py** par le chemin d'accès réel vers le script yenega-installer.py sur votre système.
Pour plus de détails, Vous pouvez utiliser la commande d'aide:

```bash
python path/vers/yenega-installer.py --help
```

**Remarque:**

Le script **yenega-installer.py** gère automatiquement l'installation des dépendances requises pour le projet. Lorsque vous créez un nouveau projet. Il clonera le framework Yenega, créera un environnement virtuel et installera les dépendances nécessaires telles que `mysql-connector-python` et `Pillow`. Si vous voyez des avertissements lors de l'installation des dépendances, vous pouvez les ignorer tant que le script signale finalement que le projet a été créé avec succès.

### 3. Suivez les Instructions

L'installateur vous guidera à travers les étapes nécessaires à la création du projet :

- Clonage du framework Yenega
- Création de l'environnement virtuel
- Installation des dépendances

### 4. Activation de l'Environnement Virtuel (si nécessaire)

Si l'activation automatique de l'environnement virtuel ne fonctionne pas, activez-le manuellement avant de travailler sur votre projet.

**Sur Windows :**
```bash
.\NomDuProjet\venv\Scripts\activate
```
**Sur Linux/macOS :**
```bash
source NomDuProjet/venv/bin/activate
```

### 5. Mise à jour des Dépendances

Pour mettre à jour l'installateur, exécutez la commande suivante :

```bash
python path/vers/yenega-installer.py update
```

## Problèmes Connus

Si vous rencontrez des problèmes lors de l'installation ou si des dépendances échouent, veuillez consulter les sections "Problèmes Courants" ou "Contributions" dans le fichier [CONTRIBUTING.md]() pour obtenir de l'aide.

## Contributions

Les contributions sont les bienvenues ! Consultez [CONTRIBUTING.md]() pour obtenir des informations sur la manière de contribuer au projet.

***

&copy; 2024 [**B. Tanguy KABORE**](https://www.linkedin.com/in/kabore-tanguy-96ab94298/)