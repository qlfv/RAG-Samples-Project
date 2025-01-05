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
