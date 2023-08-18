FROM python:3.9.17-slim

WORKDIR /code
COPY . /code

RUN apt-get update
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -e .

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=5000

CMD [ "flask", "run", "--host=0.0.0.0"]

