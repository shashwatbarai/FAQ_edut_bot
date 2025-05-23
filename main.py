import os
import getpass
from click import prompt
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import RetrievalQA
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
from regex import P
load_dotenv()


llm = ChatGoogleGenerativeAI(
    model = "gemini-2.0-flash",
    temperature = 0.1
)
# print(f"{llm=}")

loader = CSVLoader(file_path="codebasics_faqs.csv", source_column="prompt")
data = loader.load()
# print(data)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vector_store_index = FAISS.from_documents(data,embeddings)

p_rompt = """Given the following context and a question, generate an answer based on this context only.
In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

CONTEXT: {context}

QUESTION: {question}"""

PROMPT = PromptTemplate(template = p_rompt, input_variables=["context","question"])


chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store_index.as_retriever(),
    verbose=True,
    chain_type_kwargs={
        "verbose" : True,
        "prompt": PROMPT
    }
)

result = chain.invoke("Do you have Javascript courses ?")
print(result)
