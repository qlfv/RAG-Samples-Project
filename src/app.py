"""
app.py - Pipeline minimal RAG utilisant retrieval.py et generation.py
"""
from retrieval import VectorRetriever
from generation import generate_answer

documents = [
    "RAG combines document retrieval and text generation.",
    "LangChain and LlamaIndex are popular frameworks for RAG.",
    "Vector indexing allows to quickly find relevant passages.",
    "Augmented generation improves the accuracy of AI answers."
]

retriever = VectorRetriever()
retriever.fit(documents)

question = "Which frameworks can be used for RAG?"
retrieved = retriever.query(question, k=1)[0]

print("Retrieved passage:", retrieved)

answer = generate_answer(question, retrieved)
print("\nGenerated answer:\n", answer)
