from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="db",
    embedding_function=embedding_model
)

llm = ChatOpenAI(model_name="gpt-4")


def query_rag(query: str):
    docs = vectorstore.similarity_search(query, k=3)

    context = "\n".join([doc.page_content for doc in docs])

    prompt = f"""
    Use the following context to answer.

    Context:
    {context}

    Question:
    {query}
    """

    response = llm.predict(prompt)

    return response
