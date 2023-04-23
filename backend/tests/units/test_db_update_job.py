import pytest

from db.repository.jobs import create_new_job, update_job
from schemas.jobs_schema import JobCreate


@pytest.mark.parametrize('title, description, company_name, company_url, location, date_posted',
                         [('Python', 'New Python Job', 'Python', 'https://www.python.com/', 'Moscow', '2023-04-04')])
def test_db_update_job(db_session, title, description, company_name, company_url, location, date_posted):
    job = JobCreate(title=title, description=description, company_name=company_name, company_url=company_url,
                    location=location, date_posted=date_posted)
    created_job = create_new_job(job=job, db=db_session)
    update_exists_job = created_job
    update_exists_job.title = 'AnimeTitle'
    updated_job = update_job(job=update_exists_job, db=db_session)
    assert updated_job.title == 'AnimeTitle', f"The job {created_job} wasn't updated, db result is {updated_job}"
