from sqlalchemy.orm import Session

from db import Job
from schemas.jobs_schema import JobCreate


async def create_new_job(job: JobCreate, db: Session) -> Job:
    job = Job(title=job.title, company_name=job.company_name, location=job.location, date_posted=job.date_posted,
              company_url=job.company_url, description=job.description)
    db.add(instance=job)
    db.commit()
    db.refresh(instance=job)
    return job


async def retrieve_job_by_id(job_id: int, db: Session) -> Job:
    job = db.query(Job).filter(Job.id == job_id).first()
    return job


async def delete_job_by_id(job_id: int, db: Session) -> int:
    count_deleted_rows = db.query(Job).filter(Job.id == job_id).delete()
    db.commit()
    return count_deleted_rows
