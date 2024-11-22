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

## Exemple de Code

### Chargement et Segmentation de Documents PDF

Le script suivant charge un ou plusieurs fichiers PDF, les segmente en chunks, puis les stocke dans une base de données vectorielle FAISS pour permettre des recherches rapides basées sur les similarités textuelles.

```python
import os
import pickle
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_community.vectorstores import FAISS

# Chemins des fichiers et dossiers
document_path = "./pdf_samples/livre.pdf"  # Remplacez par votre chemin d'entrée
vector_db_path = "./vector_db"  # Remplacez par votre chemin de sortie
targetdb = vector_db_path + ".pkl"

# Vérification des chemins
assert os.path.exists(document_path), f"Chemin introuvable : {document_path}"

# Chargement des documents
if os.path.isdir(document_path):
    loader = PyPDFDirectoryLoader(document_path)
else:
    loader = PyPDFLoader(document_path)

documents = loader.load()

# Segmentation optimisée du texte en chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100000, chunk_overlap=0)
document_chunks = []
for doc in documents:
    chunks = text_splitter.split_documents([doc])
    document_chunks.extend(chunks)

# Création ou chargement de la base de données vectorielle
if os.path.isfile(targetdb):
    with open(targetdb, "rb") as f:
        vector_store = pickle.load(f)
    vector_store.add_documents(document_chunks)
else:
    embeddings = HuggingFaceEmbeddings(model_name="intfloat/multilingual-e5-base", model_kwargs={"device": "cpu"})
    vector_store = FAISS.from_documents(document_chunks, embeddings)

# Sauvegarde de la base de données vectorielle
with open(targetdb, "wb") as f:
    pickle.dump(vector_store, f)
```
## Recherche dans la Base de Données Vectorielle

Le script suivant montre comment interroger la base de données vectorielle pour rechercher des recettes spécifiques et afficher leurs informations pertinentes.

```python
import pickle
from langchain_community.vectorstores import FAISS

# Charger la base de données vectorielle
vector_db_path = "./vector_db.pkl"
with open(vector_db_path, "rb") as f:
    vector_store = pickle.load(f)

def get_document_by_id(doc_id):
    """
    Récupérer un document du vecteur stocké par son ID.
    
    Args:
        doc_id (any): L'ID du document à récupérer
    
    Returns:
        tuple: (document_id, document)
    """
    try:
        document = vector_store.docstore._dict[doc_id]
        return doc_id, document
    except KeyError:
        print(f"Aucun document trouvé avec l'ID '{doc_id}'.")
        return None, None

# Exemple d'utilisation
specific_doc_id = "f4cea6cb-0463-4e45-b5b2-450412522490"
document_id, document = get_document_by_id(specific_doc_id)

if document:
    print(f"Document ID : {document_id}")
    print(f"Métadonnées : {document.metadata}")
    print(f"Contenu : {document.page_content[:500]}")
```

## Contributions

Les contributions sont les bienvenues. Veuillez soumettre des demandes de tirage (PR) avec des descriptions détaillées des modifications.

## Licence

Ce projet est sous licence MIT. Veuillez vous référer au fichier LICENSE pour plus d'informations.

