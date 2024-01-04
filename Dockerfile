FROM python:3.8.18-slim

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./ /code
WORKDIR /code 
CMD bash -c "python create_db.py && python test.py && uvicorn main:app --port 8888 --host 0.0.0.0"
# CMD bash -c "python create_db.py && python test.py && gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8888"