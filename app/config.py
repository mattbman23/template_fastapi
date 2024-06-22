from dotenv import load_dotenv
import os

load_dotenv()

AUTH_SECRET = os.getenv("AUTH_SECRET", "cerave")
AGENT = os.getenv("AGENT", "logger")
AGENT_HOST_NAME = os.getenv("AGENT_HOST_NAME", "localhost")
AGENT_PORT = int(os.getenv("AGENT_PORT", 6831))
AGENT_COLLECTOR_ENDPOINT = os.getenv(
    "AGENT_COLLECTOR_ENDPOINT", "http://localhost:14268/api/traces"
)
