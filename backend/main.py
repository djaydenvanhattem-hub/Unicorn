from fastapi import FastAPI
from control-plane.global-orchestrator.service import GlobalOrchestrator

app = FastAPI()
orchestrator = GlobalOrchestrator()

@app.get("/services")
def services():
    return [{"name": "api", "status": "running"}]

@app.get("/logs")
def logs():
    return [
        {"level": "INFO", "message": "system ok"},
        {"level": "ERROR", "message": "cpu spike"}
    ]

@app.get("/metrics")
def metrics():
    return {"cpu": 0.7, "ram": 0.6}

@app.get("/ai-decisions")
def ai_decisions():
    return [
        {"id": 1, "action": "scale_up", "reason": "high cpu"}
    ]

@app.post("/approve/{id}")
def approve(id: int):
    return {"status": f"approved {id}"}
