"""
generation.py - Fonctions pour la génération de réponses augmentées (RAG)
"""
from transformers import pipeline

def generate_answer(question, context, model_name="gpt2", max_new_tokens=40):
    gen_pipe = pipeline("text-generation", model=model_name)
    prompt = f"Question : {question}\nContexte : {context}\nRéponse :"
    result = gen_pipe(prompt, max_new_tokens=max_new_tokens)[0]['generated_text']
    return result
