"""
retrieval.py - Fonctions pour l'indexation et la recherche documentaire (RAG)
"""
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorRetriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.documents = []
        self.embeddings = None

    def fit(self, documents):
        self.documents = documents
        self.embeddings = self.model.encode(documents)
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(self.embeddings)

    def query(self, question, k=1):
        q_embedding = self.model.encode([question])
        D, I = self.index.search(q_embedding, k)
        return [self.documents[i] for i in I[0]]
