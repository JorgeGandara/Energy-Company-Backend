from fastapi import FastAPI
from routers.person import router as PersonRouter
from routers.active import router as ActiveRouter

app = FastAPI()

app.include_router(PersonRouter)
app.include_router(ActiveRouter)