from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def pong():
    return {"ping": "pong"}
