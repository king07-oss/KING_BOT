FROM python:3.10-slim-buster

WORKDIR /app

RUN apt-get -y update && apt-get -y install git gcc python3-dev ffmpeg zip

COPY requirements.txt requirements.txt

RUN pip3 install -U -r requirements.txt

COPY . .

CMD [ "python3", "-m" ,
