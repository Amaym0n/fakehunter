from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db import get_db, Jobs
from db.repository.jobs import create_new_job, retrieve_job_by_id
from schemas.jobs_schema import JobCreate

jobs_router = APIRouter()


@jobs_router.post(path='/job', status_code=HTTPStatus.CREATED)
def job_create(job: JobCreate, db: Session = Depends(dependency=get_db)) -> Jobs:
    created_job = create_new_job(job=job, db=db)
    return created_job


@jobs_router.get(path='/job{job_id}', status_code=HTTPStatus.OK)
def retrieve_job(job_id: int, db: Session = Depends(dependency=get_db)) -> HTTPException | Jobs:
    retrieved_job = retrieve_job_by_id(job_id=job_id, db=db)
    if retrieved_job is None:
        return HTTPException(status_code=HTTPStatus.NOT_FOUND, detail=f'Job with id {job_id} does not exist')
    return retrieved_job
