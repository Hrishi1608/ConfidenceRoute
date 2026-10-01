from fastapi import FastAPI, WebSocket
from backend.orchestrator.orchestrator import run_task

app = FastAPI()

@app.websocket("/ws/run-task")
async def run_task_ws(websocket: WebSocket):
    await websocket.accept()
    data = await websocket.receive_json()
    task = data["task"]
    
    log = []
    answer = run_task(task, log)
    
    for entry in log:
        await websocket.send_json(entry)
        
    await websocket.send_json({"final_answer": answer})
    await websocket.close()
