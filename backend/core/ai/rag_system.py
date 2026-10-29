import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

class RAGSystem:
    def __init__(self, data_dir="data/manuals", index_path="data/faiss_index"):
        self.data_dir = data_dir
        self.index_path = index_path
        # Using a fast, standard sentence transformer model
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.vector_store = None

    def load_and_index_documents(self):
        """Loads PDFs, splits them into chunks, and embeds them into FAISS."""
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Load documents
        loader = PyPDFDirectoryLoader(self.data_dir)
        documents = loader.load()
        
        if not documents:
            print("No documents found to index.")
            return

        # Chunk the documents
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(documents)
        
        # Create and save FAISS index
        self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        self.vector_store.save_local(self.index_path)
        print(f"Indexed {len(chunks)} chunks into FAISS.")

    def get_retriever(self):
        """Returns a LangChain retriever from the loaded FAISS index."""
        if not self.vector_store:
            try:
                self.vector_store = FAISS.load_local(self.index_path, self.embeddings, allow_dangerous_deserialization=True)
            except Exception:
                print("No local FAISS index found. Please run load_and_index_documents() first.")
                return None
                
        return self.vector_store.as_retriever(search_kwargs={"k": 3})

    def search(self, query: str):
        retriever = self.get_retriever()
        if retriever:
            docs = retriever.invoke(query)
            return [doc.page_content for doc in docs]
        return []
