from sqlalchemy.orm import Session

from db.models.jobs import Jobs
from schemas.jobs import JobCreate



def create_new_job(job: JobCreate, owner_id: int, db: Session) -> Jobs:
    job = Jobs(**job.dict(), owner_id=owner_id)
    db.add(instance=job)
    db.commit()
    db.refresh(instance=job)
    return job
