from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(model='llama-3.1-8b-instant')

template = ChatPromptTemplate.from_messages([
    ("system", "You are an expert AI engineer. Always give accurate definitions. If unsure, say you don't know."),
    ("human", "{question}")
])

chain = template | llm

response = chain.invoke({
    "question": "What is RAG (Retrieval Augmented Generation) in AI?"
})

print(response.content)