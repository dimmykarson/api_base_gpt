#from app.models.features import DocumentMetadata
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv
import json
from langchain_ollama import ChatOllama

import asyncio, re

#from app.models.features import DocumentMetadata

load_dotenv()

llm = ChatOllama(
    model='deepseek-r1:8b',
)

def extract_json_from_text(response_text):
    # Expressão regular para capturar JSON dentro da resposta
    match = re.search(r"\{.*?\}", response_text, re.DOTALL)
    if match:
        try:
            json_data = json.loads(match.group())  # Tenta converter a string para um dicionário
            return json_data
        except json.JSONDecodeError:
            print("Erro ao decodificar JSON")
            return None
    else:
        print("Nenhum JSON encontrado na resposta")
        return None

def extract_document_metadata(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    text = "\n".join([page.page_content for page in pages])
    
    
    prompt = f"""
        Extraia as seguintes informações do texto do documento e retorne apenas um JSON:
    
    Instruções: 
    * Key Words são palavras chaves que resumem o conteúdo do texto.
    * Resumo é uma descrição curta do texto.

    Texto:
    {text}


    Formato da resposta:
    {{
    "title":"", 
    "autor":"", 
    "data":"", 
    "resumo":"",
    "key_words":""
    }}

    """
    
    response = llm.invoke(prompt)
    
    return extract_json_from_text(response.content)


if __name__ == "__main__":
    file_path = "/home/dimmy/Projects/api_base_gpt/tests/exemplo.pdf"
    metadata = extract_document_metadata(file_path)
    #metadata = extract_json_from_text(metadata)
    print(metadata)