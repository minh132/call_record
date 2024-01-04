FROM python:3.8.18-slim

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY ./ /code
WORKDIR /code 
CMD bash -c "python create_db.py && uvicorn main:app --port 8888 --host 0.0.0.0"