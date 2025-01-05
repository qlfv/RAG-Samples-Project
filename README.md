# RAG-Samples-Project

Ce répertoire, nommé **RAG-Samples-Project**, est dédié à la démonstration et à l'expérimentation des applications pratiques de la Génération Augmentée par Recherche (RAG - Retrieval Augmented Generation). Le projet vise à fournir des exemples concrets et des codes source en Python pour illustrer les différentes facettes de la RAG.

## Objectifs du Projet

- **Démontrer l'utilisation de la RAG** : Ce projet contient des exemples clairs de l'utilisation de la génération augmentée par la recherche pour améliorer la qualité et la précision des réponses générées à partir de documents textuels.
- **Exploration des modèles d'embeddings et de vectorisation** : Il montre comment utiliser des modèles de transformation de texte et des bases de données vectorielles pour stocker et interroger efficacement de grands volumes de texte.
- **Manipulation et extraction d'informations** : La base de données vectorielle FAISS est utilisée pour la recherche de similarités et la génération de réponses basées sur les informations pertinentes.

## Structure des Fichiers

- `rag_samples.py` : Contient les scripts de traitement, de segmentation et de vectorisation des documents PDF.
- `vector_db.pkl` : Fichier contenant la base de données vectorielle générée à partir des embeddings des documents.
- `credentials.env` : Fichier pour stocker les informations d'authentification pour le modèle génératif BAM et autres services externes.
- `README.md` : Ce fichier, qui explique la structure et les objectifs du projet.

## Prérequis

Avant de lancer les scripts, assurez-vous que les éléments suivants sont installés :

- Python 3.8 ou supérieur
- Les bibliothèques Python suivantes :
  - `langchain`
  - `langchain_community`
  - `sentence-transformers`
  - `genai`
  - `faiss`
  - `dotenv`
  - `pickle`

Installez les dépendances via pip :

```bash
pip install -r requirements.txt
```

## Exemple de Code :

### Chargement et Segmentation de Documents PDF

Le code pour charger et segmenter des documents PDF se trouve dans le fichier [`load_and_segment_documents.py`](./load_and_segment_documents.py).

### Recherche dans la Base de Données Vectorielle

Le code pour interroger la base de données vectorielle se trouve dans le fichier [`query_vector_database.py`](./query_vector_database.py).

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre des demandes de tirage (PR) avec des descriptions détaillées des modifications.

## Licence

Ce projet est sous licence MIT. Veuillez vous référer au fichier LICENSE pour plus d'informations.

