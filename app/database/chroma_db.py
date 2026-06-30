from langchain_chroma import Chroma

from app.embeddings.embedding import embedding_model

def get_vector_store():
    vector_store = Chroma(
        collection_name = 'knowledge_base',
        embedding_function=embedding_model,
        persist_directory='data/chroma_db'
    )
    return vector_store