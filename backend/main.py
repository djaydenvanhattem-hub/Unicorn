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

# ---- SaaS v6.4 Routers (Production Prefixes) ----
from organizations.routes import router as org_router
from billing.routes import router as billing_router

app.include_router(org_router, prefix="/api/orgs", tags=["Organizations"])
app.include_router(billing_router, prefix="/api/billing", tags=["Billing"])
# ------------------------------------------------
