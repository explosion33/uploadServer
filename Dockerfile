FROM ubuntu:20.04

COPY app /dir/app
COPY . /dir

RUN apt-get update -y && apt-get install python3 -y && apt-get install pip -y


WORKDIR /dir

RUN pip install -r requirements.txt



ENV PORT 8080

ENTRYPOINT [ "python3" ]

CMD ["main.py"]