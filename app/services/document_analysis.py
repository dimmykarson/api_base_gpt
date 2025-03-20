from app.models.features import DocumentMetadata
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import HuggingFaceHub
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def extract_document_metadata(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    text = "\n".join([page.page_content for page in pages])
    
    llm = HuggingFaceHub(repo_id="mistralai/Mistral-7B-Instruct-v0.1", huggingfacehub_api_token=api_token)
    
    prompt = f"""
        Extraia as seguintes informações do texto do documento e retorne apenas um JSON válido:
    {{
    "title":"", 
    "autor":"", 
    "data":"", 
    "resumo":"",
    "key_words":""
    }}

    Instruções: 
    * Key Words são palavras chaves que resumem o conteúdo do texto.
    * Resumo é uma descrição curta do texto.

    Texto:
    {text}


    ####RESPOSTA####
    """
    
    response = llm(prompt)
    
    extracted_data = response.split("####RESPOSTA####")
    extracted_data = extracted_data[1].strip()
    extracted_data = json.loads(extracted_data)
    print(":: Finalizado")
    return extracted_data