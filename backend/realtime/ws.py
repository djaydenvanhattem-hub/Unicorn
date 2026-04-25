from fastapi import WebSocket

clients = []

async def connect(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

async def broadcast(message: str):
    for c in clients:
        await c.send_text(message)
