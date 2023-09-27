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

# ENV HOST_URL="localhost"
ENV HOST_URL="https://staging.sse.uni-hildesheim.de"
ENV L3S_GATEWAY_PORT=9040
ENV L3S_AIMETA_PORT=9041
ENV L3S_RECSYS_PORT=9042
ENV L3S_SEARCH_PORT=9043

ENV L3S_AIMETA_HOST="https://staging.sse.uni-hildesheim.de:9041/l3s-aimeta/"
ENV L3S_RECSYS_HOST="https://staging.sse.uni-hildesheim.de:9042/l3s-recsys/"
ENV L3S_SEARCH_HOST="https://staging.sse.uni-hildesheim.de:9043/l3s-search/"

CMD [ "flask", "run", "--host=0.0.0.0"]




# syntax=docker/dockerfile:1.4
# FROM python:3.11.2-slim-buster AS builder

# WORKDIR /code

# COPY requirements.txt /code
# RUN pip install --upgrade pip
# RUN pip install python-dotenv
# RUN pip3 install -r requirements.txt



# COPY . /code

# ENTRYPOINT ["python3"]
# CMD ["app.py"]

