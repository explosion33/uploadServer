FROM ubuntu:20.04


RUN apt-get update -y
RUN apt-get install python3-pip -y
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nginx


COPY app /dir/app
COPY . /dir

WORKDIR /dir

RUN pip install -r requirements.txt



ENV PORT 8080
ENV DOMAIN "upload-server.ddns.net"

ENTRYPOINT [ "uwsgi" ]

CMD ["--socket", "0.0.0.0:8080", "--protocol=http", "-w", "main:app"]