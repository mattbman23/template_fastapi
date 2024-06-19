from fastapi.responses import JSONResponse
from fastapi import Header, HTTPException, status
from typing import Annotated
from config import AUTH_SECRET


def custom_response(staus_code: int, message: str):
    return JSONResponse(status_code=staus_code, content={"message": message})


def protected_route(authtoken: Annotated[str, Header()]):
    if authtoken != AUTH_SECRET:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized"
        )
    return authtoken
