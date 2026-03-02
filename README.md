# 🔎 Endee-Powered Semantic Researcher Search

A semantic search system that retrieves researchers based on contextual
meaning rather than simple keyword matching using vector embeddings.

This project demonstrates how the Endee (nD) Vector Database can be
integrated into AI/ML workflows to build scalable semantic search
systems.

------------------------------------------------------------------------

## 🚀 Project Overview

Traditional keyword-based search systems struggle to capture semantic
relationships between words.

This project solves that problem by:

-   Converting researcher interests into dense vector embeddings\
-   Managing index lifecycle using Endee\
-   Performing high-speed similarity search using FAISS\
-   Returning top matching researchers based on contextual similarity

### 🔍 Example Query

NLP healthcare transformers

### 🎯 Expected Results

Researchers working in:

-   Medical NLP\
-   Clinical AI systems\
-   Transformer-based healthcare models

------------------------------------------------------------------------

## 🧠 Problem Statement

Research discovery platforms often rely on keyword filtering, which:

-   Misses semantic similarity\
-   Fails when synonyms are used\
-   Cannot interpret contextual intent

This system uses vector embeddings + similarity search to enable
meaning-based retrieval.

------------------------------------------------------------------------

## 🏗️ System Architecture

User Query\
↓\
SentenceTransformer (all-MiniLM-L6-v2)\
↓\
Vector Embedding\
↓\
FAISS Similarity Search\
↓\
Top Matching Researchers

Endee is deployed as the vector database runtime layer for:

-   Index creation\
-   Index lifecycle management\
-   Server validation and deployment

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python\
-   SentenceTransformers\
-   FAISS (Vector Similarity Engine)\
-   Endee (nD) Vector Database\
-   Docker\
-   Pandas\
-   NumPy

------------------------------------------------------------------------

## 📦 Endee Usage (Mandatory Steps Followed)

✔ Starred official Endee repository\
✔ Forked Endee repository\
✔ Used forked repository as project base\
✔ Deployed Endee server using Docker\
✔ Created researcher index via Endee API

Endee was used for:

-   Vector database deployment\
-   Index creation\
-   Runtime validation

------------------------------------------------------------------------

## 📁 Project Structure

endee-researcher-semantic-search/ │ ├── app/ │ ├──
semantic_search_faiss.py │ ├── synthetic_researchers.csv │ ├── README.md
├── requirements.txt ├── .gitignore

------------------------------------------------------------------------

## ⚙️ Setup & Execution

### 1️⃣ Clone Repository

git clone `https://github.com/Kauriosity/endee-researcher-semantic-searcher.git`
cd app

### 2️⃣ Create Virtual Environment

python -m venv venv\
`.\venv\Scripts\Activate.ps1`

### 3️⃣ Install Dependencies

pip install sentence-transformers faiss-cpu pandas numpy

### 4️⃣ Run Semantic Search

python semantic_search_faiss.py

Try queries such as:

-   Graph neural networks\
-   AI climate modeling\
-   Healthcare NLP transformers

------------------------------------------------------------------------

## 🔍 Key Features

-   Meaning-based semantic retrieval\
-   High-speed vector similarity search\
-   Clean and modular architecture\
-   Dockerized vector database runtime\
-   Easily extendable to RAG or recommendation systems

------------------------------------------------------------------------

## 🎯 Future Improvements

-   Hybrid Search (BM25 + Vector Search)\
-   REST API integration\
-   Web-based frontend interface\
-   Retrieval-Augmented Generation (RAG)\
-   Production deployment with scalability

------------------------------------------------------------------------

## 📜 License

This project builds upon Endee (Apache License 2.0).\
Endee branding and trademarks belong to Endee Labs.
