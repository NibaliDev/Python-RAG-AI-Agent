# Python-RAG-AI-Agent
Här experimenterar jag med API:er, databaser och databashantering för att skapa en RAG AI-Agent.

Inngest

# Tools
Python (stack)
- Huvudsakliga utvecklingsmiljö
Streamlit (frontend)
Qdrant
- Specifik vektordatabas vilken går att köras lokalt
Ingest
- Orkestrering och observerbarhet
Llamaindex
- Ingesting PDF:S
OpenAI
- AI Components


# Mer om RAG AI-Agents
[Wikipedia](https://en.wikipedia.org/wiki/Retrieval-augmented_generation)

PDF --> vector database --> prompt --> ChatGPT --> answer

# Komandon

uv run uvicorn main:app

npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery

docker run .d --name -p 6333:6333 -v "$(pwd)/qdrant_storage:/qdrant/storage