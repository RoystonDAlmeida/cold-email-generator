# Cold Email Generator

This repository creates a cold email in response to any job posting url.
<br>

## Features
1. **WebBaseLoader**: Scrapes text from a particular url.

**Usage**: 

```bash
from langchain_community.document_loaders import WebBaseLoader
loader = WebBaseLoader([url_input])
data = clean_text(loader.load().pop().page_content)
```

2. **Chromadb**: A vector DB that is used to store collections.

**Usage**: 

```bash
import chromadb
chroma_client = chromadb.PersistentClient('vectorstore')
collection = self.chroma_client.get_or_create_collection(name="portfolio")
```

3. **Chatgroq**: A class from language through which we can interact with various AI models.

**Usage**:

```bash
from langchain_groq import ChatGroq
```

## Environment Variables

To run this application, you need to create a `.env` file in the root directory of your project. This file should contain the following environment variables:

```bash
GROQ_API_KEY =
URL =
```

## Installation
1. Clone the repository using `git clone`
2. Execute the `main.py` file using `streamlit run main.py`. It will run on `Port: 8501`