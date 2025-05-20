# RAG-Samples-Project

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/qlfv/RAG-Samples-Project/blob/main/demo_rag.ipynb)

Ce projet démontre la Génération Augmentée par Recherche (RAG) : comment combiner recherche documentaire et génération de texte pour des réponses plus précises.

---

## 🚀 Quickstart

```bash
# Clone le repo
git clone https://github.com/qlfv/RAG-Samples-Project.git
cd RAG-Samples-Project

# Installe les dépendances (environnement Python >=3.8)
pip install -r requirements.txt
```

Ou ouvre directement le notebook sur [Google Colab](https://colab.research.google.com/github/qlfv/RAG-Samples-Project/blob/main/demo_rag.ipynb).

---

## 🧠 Schéma du pipeline RAG

```
[Question utilisateur]
          |
   [Embeddings]
          |
   [Recherche dans index vectoriel]
          |
   [Passage retrouvé]
          |
   [Génération de réponse (LLM)]
          |
   [Réponse augmentée]
```

---

## 📚 Pour aller plus loin

- [LangChain](https://python.langchain.com/)
- [LlamaIndex](https://www.llamaindex.ai/)
- [Haystack](https://haystack.deepset.ai/)
- [Paper original RAG (Facebook)](https://arxiv.org/abs/2005.11401)

---

## 📂 Structure recommandée

- `demo_rag.ipynb` : Notebook de démo minimal
- `src/` : Scripts Python modulaires (retrieval.py, generation.py…)
- `data/` : Mini-datasets d’exemple
- `README.md` : Documentation, schémas, liens

---

## 📝 Licence

Ce projet est open source (MIT).

---

**N’hésitez pas à proposer des améliorations ou à ouvrir des issues !**
- **Manipulation et extraction d'informations** : La base de données vectorielle FAISS est utilisée pour la recherche de similarités et la génération de réponses basées sur les informations pertinentes.

## Structure des Fichiers

- `load_and_segment_documents.py` : Script pour le chargement, la segmentation et la vectorisation des documents PDF.
- `query_vector_database.py` : Script pour interroger la base de données vectorielle et récupérer les informations pertinentes.
- `vector_db.pkl` : Fichier contenant la base de données vectorielle générée à partir des embeddings des documents.
- `README.md` : Ce fichier, qui explique la structure et les objectifs du projet.
- `requirements.txt` : Liste des dépendances Python nécessaires pour exécuter les scripts.

## Prérequis

Avant de lancer les scripts, assurez-vous que les éléments suivants sont installés :

- **Python** 3.8 ou supérieur
- Les bibliothèques Python listées dans `requirements.txt`.

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

