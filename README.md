# Document Analysis API

## 📌 Sobre o Projeto

Esta API permite a extração de metadados de documentos em PDF usando modelos de linguagem natural, como **DeepSeek-R1** (via **Ollama**) e **GPT-4o** (via **OpenAI**). A API processa o documento e retorna um JSON contendo informações como título, autor, data, resumo e palavras-chave.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.10+**
- **Flask** - Framework para criação da API
- **LangChain** - Para integração com modelos de IA
- **Ollama** - Para execução do modelo DeepSeek-R1 localmente
- **OpenAI GPT-4o** - Para análise alternativa via API OpenAI
- **PyPDFLoader** - Para extração de texto de PDFs
- **Dotenv** - Para gerenciamento de variáveis de ambiente

---

## 📂 Estrutura do Projeto
```
project-root/
│── app/
│   ├── routes.py
│   ├── services/
│   │   ├── document_analysis_deepseek.py
│   │   ├── document_analysis_gpt.py
│   ├── utils/
│   │   ├── file_utils.py
│── uploads/   # Diretório onde os PDFs enviados são armazenados temporariamente
│── main.py
│── requirements.txt
│── .env
│── README.md
```

---

## ⚙️ Configuração e Execução

### 1️⃣ Instale as dependências
```sh
pip install -r requirements.txt
```

### 2️⃣ Configure as variáveis de ambiente
Crie um arquivo `.env` na raiz do projeto e adicione:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3️⃣ Inicie o servidor Flask
```sh
python main.py
```

A API estará disponível em: `http://127.0.0.1:5000/`

---

## 🛠️ Rotas Disponíveis

### 📌 **Rota Principal**
**`GET /`**  
Retorna uma mensagem de boas-vindas.

**Resposta:**
```json
{
  "message": "Hello, World!"
}
```

---

### 📌 **Análise de Documento com DeepSeek-R1**
**`POST /analise`**  
Envia um arquivo PDF e retorna os metadados extraídos usando o **modelo DeepSeek-R1 via Ollama**.

#### 📌 **Requisição:**
- `Content-Type: multipart/form-data`
- Parâmetro: `file` (arquivo PDF)

#### 📌 **Resposta:**
```json
{
    "title": "Título do Documento",
    "autor": "Nome do Autor",
    "data": "2025-03-19",
    "resumo": "Resumo do conteúdo do documento...",
    "key_words": ["palavra1", "palavra2", "palavra3"]
}
```

---

### 📌 **Análise de Documento com GPT-4o**
**`POST /analise/gpt`**  
Envia um arquivo PDF e retorna os metadados extraídos usando **GPT-4o via OpenAI API**.

#### 📌 **Requisição:**
- `Content-Type: multipart/form-data`
- Parâmetro: `file` (arquivo PDF)

#### 📌 **Resposta:**
```json
{
    "title": "Título do Documento",
    "autor": "Nome do Autor",
    "data": "2025-03-19",
    "resumo": "Resumo do conteúdo do documento...",
    "key_words": ["palavra1", "palavra2", "palavra3"]
}
```

---

## 🔍 Funcionamento Interno

1️⃣ O arquivo PDF é recebido via `POST` e salvo no diretório `/uploads`.
2️⃣ O **PyPDFLoader** extrai o texto do documento.
3️⃣ O texto é enviado para um **modelo de IA** (DeepSeek-R1 via **Ollama** ou **GPT-4o** via OpenAI).
4️⃣ O modelo processa o texto e retorna os metadados em JSON.

---

## 🛠️ Como Rodar Testes Locais

Se quiser testar a API sem um frontend, você pode usar o **cURL** ou **Postman**:

```sh
curl -X POST "http://127.0.0.1:5000/analise" \
     -F "file=@caminho/do/seu/arquivo.pdf"
```

Para a versão com GPT-4o:
```sh
curl -X POST "http://127.0.0.1:5000/analise/gpt" \
     -F "file=@caminho/do/seu/arquivo.pdf"
```

---

## 🔥 Futuras Melhorias
✅ Melhorar a extração automática do autor e da data.
✅ Implementar cache para evitar reprocessamento do mesmo documento.
✅ Suporte para mais formatos de arquivo (Word, TXT, etc.).
✅ Interface Web para upload de arquivos e visualização dos resultados.

---

## 📄 Licença
Este projeto está licenciado sob a **MIT License**.

