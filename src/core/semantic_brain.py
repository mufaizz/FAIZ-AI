import numpy as np
from sentence_transformers import SentenceTransformer
import json
import os

class SemanticBrain:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.embedding_dim = self.model.get_sentence_embedding_dimension()

    def get_embedding(self, text):
        if not text or not isinstance(text, str):
            return np.zeros(self.embedding_dim)
        embedding = self.model.encode(text, normalize_embeddings=True)
        return embedding

    def similarity(self, embedding_a, embedding_b):
        return np.dot(embedding_a, embedding_b)

    def batch_embed(self, texts):
        if not texts:
            return []
        return self.model.encode(texts, normalize_embeddings=True)

    def save_vectors(self, vectors, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        np.save(filepath, vectors)

    def load_vectors(self, filepath):
        if os.path.exists(filepath):
            return np.load(filepath)
        return None