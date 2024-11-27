# Cold Email Generator

This repository creates a cold email in response to any job posting url.
<br>

## Features
1. **WebBaseLoader**: Scrapes text from a particular url.
<br>
**Usage**: from langchain_community.document_loaders import WebBaseLoader
<br>
loader = WebBaseLoader([url_input])
<br>
data = clean_text(loader.load().pop().page_content)
<br>
<br>
2. **Chromadb**: A vector DB that is used to store collections.
<br>
**Usage**: import chromadb
<br>
chroma_client = chromadb.PersistentClient('vectorstore')
<br>
collection = self.chroma_client.get_or_create_collection(name="portfolio")
<br>
<br>
3. **Chatgroq**: A class from language through which we can interact with various AI models.
<br>
from langchain_groq import ChatGroq
<br>

## Installation
1. Clone the repository using `git clone`
<br>
2. Execute the `main.py` file using `streamlit run main.py`. It will run on `Port: 8501`


