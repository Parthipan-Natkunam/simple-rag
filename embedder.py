from llama_index.core import (
    load_index_from_storage
)
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.readers import SimpleDirectoryReader
from llama_index.core.indices.vector_store import VectorStoreIndex
from llama_index.core.storage import StorageContext
import os

source_dir = './retrievables/'
vector_indices = './vector_indices/'


embed_model=HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

def get_embed_model():
    return embed_model

def create_vector_embeddings():
    vector_store = None
    if os.path.exists(vector_indices):
        print(f"Reading VectorStore from {vector_indices}")
        storage_context = StorageContext.from_defaults(
            persist_dir=vector_indices,
        )
        vector_store = load_index_from_storage(
            storage_context=storage_context
        )
    else:
        print(f"Reading documents in: {source_dir}")
        documents = SimpleDirectoryReader(source_dir).load_data()
        vector_store = VectorStoreIndex.from_documents(documents)
        print(f"Persisting vector store to: {vector_indices}")
        os.mkdir(vector_indices)
        vector_store.storage_context.persist(persist_dir=vector_indices)
        vector_store
    return vector_store


