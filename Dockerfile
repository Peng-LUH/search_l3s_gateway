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
ENV POSTGRES_HOST="l3s-search-db"
ENV L3S_GATEWAY_HOST_NAME="localhost"
ENV L3S_GATEWAY_PORT=9040
ENV L3S_AIMETA_PORT=9041
ENV L3S_RECSYS_PORT=9042
ENV L3S_SEARCH_PORT=9043
ENV L3S_AIMETA_HOST="https://staging.sse.uni-hildesheim.de:9041/l3s-aimeta/"
ENV L3S_RECSYS_HOST="https://staging.sse.uni-hildesheim.de:9042/l3s-recsys/"
ENV L3S_SEARCH_HOST="https://staging.sse.uni-hildesheim.de:9043/l3s-search/"

CMD ["flask", "run", "--port=9040", "--host=0.0.0.0"]

EXPOSE 9040

