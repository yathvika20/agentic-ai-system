from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from backend.api.routers import health
from backend.api.routers import chat



app = FastAPI(

    title="Agentic AI API",

    version="1.0.0"

)



app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)



app.include_router(health.router)

app.include_router(

        chat.router,

        prefix="/api/v1"

)
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