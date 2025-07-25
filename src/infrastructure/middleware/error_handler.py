from fastapi import Request
from fastapi.responses import JSONResponse

from src.infrastructure.logging.logger import logger


async def global_exception_handler(request: Request, exc: Exception):
    logger.error(
        "Unhandled exception",
        path=request.url.path,
        method=request.method,
        error=str(exc),
        exc_info=True
    )

    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )
