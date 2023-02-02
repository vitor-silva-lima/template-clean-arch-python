FROM ubuntu:20.04

RUN apt update \
 && apt upgrade -y \
 && apt install curl -y 

RUN apt-get update

RUN apt install -y -q build-essential python3-pip python3-dev

RUN pip3 install -U pip setuptools wheel

RUN pip3 install gunicorn uvloop httptools

WORKDIR /app

# COPY requirements.txt /app/requirements.txt

# RUN pip3 install -r /app/requirements.txt

COPY ./ /app

EXPOSE 80

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:80", "--timeout", "0", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--graceful-timeout", "0"]
