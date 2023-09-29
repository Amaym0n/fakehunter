from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic.types import conint
from db import get_db, Jobs
from db.repository.jobs import create_new_job, retrieve_job_by_id, delete_job_by_id
from schemas.jobs_schema import JobCreate

jobs_router = APIRouter()


@jobs_router.post(path='/job/', status_code=HTTPStatus.CREATED)
async def job_create(job: JobCreate, db: Session = Depends(dependency=get_db)) -> Jobs:
    return await create_new_job(job=job, db=db)


@jobs_router.get(path='/job/{job_id}', status_code=HTTPStatus.OK)
async def retrieve_job(job_id: conint(gt=0), db: Session = Depends(dependency=get_db)) -> HTTPException | Jobs:
    retrieved_job = await retrieve_job_by_id(job_id=job_id, db=db)
    if retrieved_job is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f'Job with id {job_id} does not exist')
    return retrieved_job


@jobs_router.delete(path='/job/{job_id}', status_code=HTTPStatus.NO_CONTENT)
async def delete_job(job_id: conint(gt=0), db: Session = Depends(dependency=get_db)) -> HTTPException | int:
    count_deleted_rows = await delete_job_by_id(job_id=job_id, db=db)
    if count_deleted_rows == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail=f"Job with id {job_id} does not exist")
    return count_deleted_rows
