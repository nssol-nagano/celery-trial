from fastapi import FastAPI
from fastapi.responses import JSONResponse
from tasks import celery_app, sleep_a_sec

app = FastAPI()


@app.get("/run/")
def process_task():
    task = sleep_a_sec.delay()
    return JSONResponse(content={"task_id": task.id})


@app.get("/result/{task_id}")
def get_task_result(task_id: str):
    task_result = celery_app.AsyncResult(task_id)

    if task_result.state == "PENDING":
        return {"task_id": task_id, "status": task_result.state, "result": None}
    elif task_result.state != "FAILURE":
        return {
            "task_id": task_id,
            "status": task_result.state,
            "result": task_result.result,
        }
    else:
        return {
            "task_id": task_id,
            "status": task_result.state,
            "result": str(task_result.result),
        }
