from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from api import router as api_router
from core.config import settings
from core.models import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    await db_helper.dispose()


app = FastAPI(
    default_response_class=ORJSONResponse,
    lifespan=lifespan,
)
app.include_router(
    router=api_router,
)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True,
    )
