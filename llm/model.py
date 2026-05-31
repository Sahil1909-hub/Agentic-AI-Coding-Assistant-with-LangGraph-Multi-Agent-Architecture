from utils.config import GROQ_API_KEY
from langchain_groq import ChatGroq


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=GROQ_API_KEY,
    temperature=0
)