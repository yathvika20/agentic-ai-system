from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from slowapi import Limiter
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

from backend.api.routers import health
from backend.api.routers import chat

from backend.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="Agentic AI API",
    version="1.0.0"
)

####################################################
# Rate Limiter
####################################################

from backend.api.limiter import limiter

app = FastAPI(
    title="Agentic AI API",
    version="1.0.0"
)

####################################################
# Attach Limiter
####################################################

app.state.limiter = limiter

app.add_exception_handler(
    RateLimitExceeded,
    lambda request, exc: JSONResponse(
        status_code=429,
        content={
            "detail": "Rate limit exceeded. Please try again later."
        },
    ),
)

app.add_middleware(SlowAPIMiddleware)

####################################################
# CORS
####################################################

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

####################################################
# Routers
####################################################

app.include_router(health.router)

app.include_router(
    chat.router,
    prefix="/api/v1"
)

####################################################
# Global Exception Handler
####################################################

@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception
):
    return JSONResponse(
        status_code=500,
        content={
            "error": str(exc),
            "path": request.url.path
        }
    )