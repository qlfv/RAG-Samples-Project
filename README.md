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

## ⚠️ Limites des modèles utilisés et bonnes pratiques

- Le modèle par défaut utilisé pour la génération est **GPT-2** (HuggingFace). Il n'est pas spécialisé pour le français ni pour le question/réponse technique : il fonctionne nettement mieux en anglais.
- **Hallucinations** : GPT-2 peut inventer des réponses ou des noms de frameworks qui n'existent pas (ex : "LlamaTk").
- **Compréhension limitée** : il peut générer des phrases grammaticalement correctes mais sans sens technique précis.
- **Prompting** : la qualité du prompt (instructions, formulation) influence fortement la pertinence de la réponse.
- **Pas de connaissances récentes** : GPT-2 ne connaît pas les frameworks ou concepts apparus après 2019.

### Bonnes pratiques pour de meilleurs résultats

- Privilégier l'anglais pour la génération avec GPT-2.
- Pour le français, utiliser un modèle francophone (ex : `cmarkea/gpt2-small-french`) ou un pipeline "question-answering" (`illuin/camembert-base-fquad`).
- Structurer les prompts : donner des instructions claires, préciser le contexte et la question.
- Tester plusieurs modèles selon la tâche (génération libre vs Q&A).
- Toujours valider la réponse générée avant de la présenter à un utilisateur final.

---

## ❓ FAQ sur la génération IA (RAG)

**Q : Pourquoi la réponse générée n’est-elle pas toujours pertinente ?**
> Les modèles comme GPT-2 ne comprennent pas réellement le sens : ils prédisent la suite la plus probable du texte. Ils peuvent donc générer des phrases correctes mais factuellement fausses ou hors sujet.

**Q : Comment éviter que le modèle “invente” des informations ?**
> Utilisez des modèles spécialisés pour le question/réponse (pipeline "question-answering") et structurez bien le prompt. Pour des tâches critiques, validez toujours la réponse générée.

**Q : Peut-on utiliser d’autres modèles que GPT-2 ?**
> Oui ! Essayez des modèles plus récents ou spécialisés (GPT-J, Falcon, Mistral, modèles francophones, etc.) disponibles sur HuggingFace.

**Q : Comment améliorer la génération en français ?**
> Utilisez un modèle francophone (ex : `cmarkea/gpt2-small-french`) ou un modèle Q&A entraîné sur des données françaises (`illuin/camembert-base-fquad`).

**Q : Pourquoi le modèle ne connaît-il pas les frameworks récents ?**
> Les modèles ont été entraînés sur des données arrêtées à une certaine date (ex : 2019 pour GPT-2). Ils ne connaissent pas les nouveautés apparues après.

**Q : Peut-on utiliser RAG avec des documents PDF ou des sites web ?**
> Oui, il suffit d’extraire le texte des documents et de l’indexer avec la même logique (voir les frameworks comme LangChain ou LlamaIndex pour des pipelines avancés).

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

