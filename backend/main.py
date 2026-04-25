from fastapi import FastAPI, WebSocket
from auth.routes import router as auth_router
from realtime.ws import connect

app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def root():
    return {"status": "ok"}

@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await connect(ws)
