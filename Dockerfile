FROM python:3.9-slim

# RUN apt update && apt install -y apt-transport-https

# RUN apt -y install sudo

# RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

# USER docker

# RUN apt install postgresql postgresql-contrib -y

# RUN sudo -i -u postgres

WORKDIR /app

ADD . /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5432

ENV NAME venv

CMD ["python3", "main.py"]

