FROM python:3.11.2-slim-buster

WORKDIR /code
COPY . /code

RUN pip install --upgrade pip setuptools wheel
RUN pip install -e .

ENV FLASK_APP=run.py
CMD [ "flask", "run", "--host=0.0.0.0"]

