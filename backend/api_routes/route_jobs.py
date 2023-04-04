from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import get_db, Jobs
from db.repository.jobs import create_new_job
from schemas.jobs_schema import JobCreate

jobs_router = APIRouter()


@jobs_router.post(path='/job', status_code=HTTPStatus.CREATED)
def job_create(job: JobCreate, db: Session = Depends(dependency=get_db)) -> Jobs:
    created_job = create_new_job(job=job, db=db)
    return created_job
