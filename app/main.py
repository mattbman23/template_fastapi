from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from config import AGENT, AGENT_HOST_NAME, AGENT_PORT
from fastapi.middleware.cors import CORSMiddleware
from opentelemetry.sdk.trace import TracerProvider
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from utils import protected_route
from opentelemetry import trace
from api import ping, llm

# Set up the tracer provider
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: AGENT}))
)
tracer_provider = trace.get_tracer_provider()

# Configure Jaeger exporter
jaeger_exporter = JaegerExporter(
    agent_host_name=AGENT_HOST_NAME,
    agent_port=AGENT_PORT,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Run... before app starts")
    tracer_provider.add_span_processor(BatchSpanProcessor(jaeger_exporter))
    yield
    print("Run... before app ends")


# Create a FastAPI app and instrument it
app = FastAPI(lifespan=lifespan)
FastAPIInstrumentor.instrument_app(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
    allow_methods=["GET", "POST"],
)

app.include_router(llm.router, prefix="/llm", dependencies=[Depends(protected_route)])
app.include_router(ping.router, prefix="/ping")
