import logging
from fastapi import FastAPI
import inngest
import inngest.fast_api
from inngest.experimental import ai
from dotenv import load_dotenv
import uuid
import datetime

load_dotenv() # Load .env file

inngest_client = inngest.Inngest(
    app_id = "rag_app",
    logger = logging.getLogger("uvicorn"),
    is_production = False,
    serializer = inngest.PydanticSerializer()
)

# Pydantic: define the types of different variables

# Inngest tar hand om loggning för denna funktion
@inngest_client.create_function(
    fn_id = "RAG: Inngest PDF",
    trigger = inngest.TriggerEvent(event="rag/ingest_pdf")
)
async def rag_inngest_pdf(ctx: inngest.Context):
    return {"hello": "world"}

app = FastAPI()

inngest.fast_api.serve(app, inngest_client, functions=[rag_inngest_pdf])

# Inngest functions connects to an Inngest development server


