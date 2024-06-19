from fastapi import APIRouter
from opentelemetry import trace

router = APIRouter()

tracer = trace.get_tracer(__name__)


@router.get("/generate_text")
def generate_text():
    with tracer.start_as_current_span("Generating text"):
        return {"message": "Lorem..."}
