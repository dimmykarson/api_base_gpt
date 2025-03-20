from pydantic import BaseModel, Field

class DocumentMetadata(BaseModel):
    title: str = Field(description="Título do documento")
    autor: str = Field(description="Autor do documento")
    data: str = Field(description="Data de criação do documento")
    subject: str = Field(description="Assunto do documento")
    key_words: str = Field(description="Palavras-chave do documento")
