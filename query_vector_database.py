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
