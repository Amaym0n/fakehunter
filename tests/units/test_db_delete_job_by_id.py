import pytest

from db.repository.jobs import create_new_job, delete_job_by_id
from schemas.jobs_schema import JobCreate


@pytest.mark.parametrize('title, description, company_name, company_url, location, date_posted',
                         [('Python', 'New Python Job', 'Python', 'https://www.python.com/', 'Moscow', '2023-04-04')])
def test_db_delete_job_by_id(db_session, title, description, company_name, company_url, location, date_posted):
    job = JobCreate(title=title, description=description, company_name=company_name, company_url=company_url,
                    location=location, date_posted=date_posted)
    created_job = create_new_job(job=job, db=db_session)
    count_deleted_rows = delete_job_by_id(job_id=created_job.id, db=db_session)
    assert count_deleted_rows != 0, f"The job {created_job} wasn't deleted"
