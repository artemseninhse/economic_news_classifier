FROM python:3.9-slim

RUN apt install postgresql postgresql-contrib -y

RUN sudo -i -u postgres

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5432

ENV NAME venv

CMD ["python3", "main.py"]

