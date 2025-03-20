from app.models.features import DocumentMetadata
from langchain.document_loaders import PyPDFLoader
from dotenv import load_dotenv
import json, os
from langchain.utils.openai_functions import convert_pydantic_to_openai_function
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model='gpt-4o',
    api_key=os.getenv("OPENAI_API_KEY")
)

prompt = f"""
    Extraia as informações do texto do documento e retorne apenas um JSON.
    
    Instruções: 
    * Key Words são palavras chaves que resumem o conteúdo do texto.
    * Resumo é uma descrição curta do texto.

    Texto:
    """
dataextract_function = [
        convert_pydantic_to_openai_function(DocumentMetadata)
]

prompt_template = ChatPromptTemplate.from_messages([
        ("system", prompt),
        ("human", "{input}"),
])

model = llm.bind(
        functions=dataextract_function,
        function_call={"name": "DocumentMetadata"}
    )
chain = prompt_template | model


def extract_document_metadata_gpt(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    
    text = "\n".join([page.page_content for page in pages])
    
    result = chain.invoke({"input": text})
    dataextract_json = result.additional_kwargs["function_call"]["arguments"]
    return json.loads(dataextract_json)

    
    