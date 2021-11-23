FROM ubuntu:20.04

COPY app /dir/app
COPY . /dir


RUN apt-get update -y
RUN apt-get install python3 -y && apt-get install pip -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nginx


WORKDIR /dir

RUN pip install -r requirements.txt



ENV PORT 8080

ENTRYPOINT [ "uwsgi" ]

CMD ["--socket", "0.0.0.0:8080", "--protocol=http", "-w", "main:app"]