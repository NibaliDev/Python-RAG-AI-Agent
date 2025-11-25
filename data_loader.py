from openai import OpenAI
from llama_index.readers.file import PDFReader
from llama_index.core.node_parser import SentenceSplitter
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

EMBED_MODEL = "text-embedding-3-large"
EMBED_DIM = 3072

# chunk_overlap på 200 tecken för att inte förlora kontext.
splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=200)

#reader = PDFReader()
#Dela upp PDF-dokumentet i chunks. Annars blir datamängden för stor.
#Llamaindex for loading PDF-files

def load_and_chunk_pdf(path: str):
    docs = PDFReader().load_data(file=path)
    texts = [d.text for d in docs if getattr(d, "text", None)] # Se till att d innehåller text
    chunks = []
    for t in texts:
        chunks.extend(splitter.split_text(t))
    return chunks

def embed_text(texts: list[str]) -> list[float]:
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]

