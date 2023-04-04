from db import Jobs
from db.session import Session
from schemas.jobs_schema import JobCreate


def create_new_job(job: JobCreate, db: Session) -> Jobs:
    job = Jobs(title=job.title, company_name=job.company_name, location=job.location, date_posted=job.date_posted,
               company_url=job.company_url, description=job.description)
    db.add(instance=job)
    db.commit()
    db.refresh(instance=job)
    return job
