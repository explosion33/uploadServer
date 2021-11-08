FROM ubuntu:16.04
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV PORT 8080

RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "main.py"]