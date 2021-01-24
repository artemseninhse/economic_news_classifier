FROM python

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN apt install postgresql -y

RUN postgresql-contrib -y

RUN sudo -i -u postgres

EXPOSE 5432

ENV NAME venv

CMD ["python3", "main.py"]

