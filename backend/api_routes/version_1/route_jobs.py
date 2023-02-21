from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.jobs import create_new_job
from db.session import get_db
from schemas.jobs import JobCreate, ShowJob

router = APIRouter()


@router.post(path='/create', response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(dependency=get_db)):
    job = create_new_job(job=job, owner_id=1, db=db)
    return job
