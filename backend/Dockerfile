FROM python:3.11
WORKDIR /fakehunter
COPY ./requirements.txt /fakehunter/requirements.txt
RUN pip install --no-cache-dir --upgrade -r
COPY ./* /fakehunter
CMD ["uvicorn", "fakehunter.main:app", "--host", "0.0.0.0", "--port", "80"]