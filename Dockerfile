FROM ubuntu:20.04

RUN apt update \
 && apt upgrade -y \
 && apt install curl -y \
 && apt install zip -y \
 && apt install unzip -y \
 && apt install cifs-utils -y \
 && apt-get install libgssapi-krb5-2 -y \
 && apt install unixodbc -y \
 && apt install unixodbc-dev -y \
 && apt install freetds-dev -y \
 && apt install freetds-bin -y \
 && apt install tdsodbc -y \
 && apt install curl -y \
 && apt install apt-transport-https -y \
 && apt install gnupg -y 

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt install -y --allow-unauthenticated msodbcsql17
RUN ACCEPT_EULA=Y apt install -y --allow-unauthenticated mssql-tools
RUN ACCEPT_EULA=Y apt install -y --allow-unauthenticated libssl1.1
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

RUN apt update

RUN apt install -y -q build-essential python3-pip python3-dev

RUN pip3 install -U pip setuptools wheel

RUN pip3 install gunicorn uvloop httptools

WORKDIR /app

# COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt

COPY ./ /app

EXPOSE 80

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:80", "--timeout", "0", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "--graceful-timeout", "0"]
