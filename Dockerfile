FROM python

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5432

ENV NAME venv

CMD ["python", "main.py"]

