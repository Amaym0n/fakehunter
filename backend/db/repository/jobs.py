from sqlalchemy.orm import Session

from db import Jobs
from schemas.jobs_schema import JobCreate


def create_new_job(job: JobCreate, db: Session) -> Jobs:
    job = Jobs(title=job.title, company_name=job.company_name, location=job.location, date_posted=job.date_posted,
               company_url=job.company_url, description=job.description)
    db.add(instance=job)
    db.commit()
    db.refresh(instance=job)
    return job


def retrieve_job_by_id(job_id: int, db: Session) -> Jobs:
    job = db.query(Jobs).filter(Jobs.id == job_id).first()
    return job
