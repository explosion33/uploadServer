# uploadServer
A small file upload server similar to the likes of Google Drive or Dropbox, but without requiring a login or subscription, or limiting file size.


This project is mainly for personal use.


## Tech
This webserver is run using a backend of flask and a frontend of Html, Jinja, JS, and Bootstrap.

Using the [docker file](https://hub.docker.com/repository/docker/explosion33/upload-server) the Server can be hosted with Nginx and uWSGI

## Run
This server can be run locally using

```
docker pull explosion33/upload-server
docker run -p 80:8080 explosion33/uplosd-server:latest
```

or built locally

```
git clone https://github.com/explosion33/uploadServer.git
docker build -t name:tag .
docker run -p 80:8080 name:tag
```

## Development

For ease of development use flask's built in server
```
pip install -r requirements.txt
```

```
python3 main.py
```

then access the site at
```
localhost:5000
```
