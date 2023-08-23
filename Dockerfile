FROM python:3.9.17-slim

WORKDIR /code
COPY . /code

RUN apt-get update
RUN apt-get -y install python3-dev
RUN pip install --upgrade pip setuptools wheel
RUN pip install -e .

ENV FLASK_APP=run.py
ENV FLASK_DEBUG=1
ENV FLASK_RUN_PORT=9040

ENV HOST_IP="localhost"
ENV L3S_GATEWAY_PORT=9040
ENV L3S_AIMETA_PORT=9041
ENV L3S_RECSYS_PORT=9042
ENV L3S_SEARCH_PORT=9043

CMD [ "flask", "run", "--host=0.0.0.0"]

