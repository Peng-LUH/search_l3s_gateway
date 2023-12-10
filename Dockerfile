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
# ENV POSTGRES_HOST=localhost

ENV L3S_GATEWAY_HOST_NAME="localhost"
ENV L3S_GATEWAY_PORT=9040
ENV L3S_AIMETA_PORT=9041
ENV L3S_RECSYS_PORT=9042
ENV L3S_SEARCH_PORT=9043

ENV L3S_AIMETA_HOST="https://staging.sse.uni-hildesheim.de:9041/l3s-aimeta/"
ENV L3S_RECSYS_HOST="https://staging.sse.uni-hildesheim.de:9042/l3s-recsys/"
ENV L3S_SEARCH_HOST="https://staging.sse.uni-hildesheim.de:9043/l3s-search/"
ENV SSE_HOST_URL="https://staging.sse.uni-hildesheim.de"
# RUN python3 -m flask db init

# CMD flask db init; flask db migrate; flask run
# CMD ["/bin/bash", "-c", "flask run"]

# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]

# CMD ["/bin/bash", "-c", "flask run --host 0.0.0.0 --port 9040"]
CMD ["flask", "run", "--port=9040", "--host=0.0.0.0"]
# CMD ["sh", "-c", "python test.py"]
EXPOSE 9040

# RUN flask db init
# RUN flask db migrate
# RUN flask db stamp head

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

