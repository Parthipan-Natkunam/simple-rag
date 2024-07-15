from llama_index.core import (
    Settings
)
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.chat_engine import ContextChatEngine
from ai import get_llm
from embedder import get_embed_model, create_vector_embeddings



def setup_llama_index():
    Settings.llm = get_llm()
    Settings.chunk_size = 512
    Settings.chunk_overlap = 64
    Settings.embed_model = get_embed_model()    

def main():
    setup_llama_index()
    vector_store = create_vector_embeddings()
    retriever = VectorIndexRetriever(vector_store)
    query_engine = RetrieverQueryEngine.from_args(
        retriever=retriever
    )

    chat_engine = ContextChatEngine.from_defaults(
        retriever=retriever,
        query_engine=query_engine,
        verbose=True
    )

    chat_engine.chat_repl()



if __name__ == "__main__":
    main()