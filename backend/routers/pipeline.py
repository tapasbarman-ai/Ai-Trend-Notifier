from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
from .. import database, models
from .auth import get_current_user
import sys
import os
import subprocess

router = APIRouter(
    prefix="/pipeline",
    tags=["pipeline"],
)

def run_pipeline_task():
    # Run the integrated pipeline script as a subprocess
    try:
        subprocess.run([sys.executable, "run_pipeline_integrated.py"], check=True)
    except Exception as e:
        print(f"Error running pipeline: {e}")

@router.post("/run")
def trigger_pipeline(background_tasks: BackgroundTasks, current_user: models.User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Not authorized")
    
    background_tasks.add_task(run_pipeline_task)
    return {"message": "Pipeline triggered in background"}
