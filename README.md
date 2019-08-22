# Sample Flask Docker API

## Getting started
Clone the repo
```
git clone git@github.com:anothercuriousneuron/flask-docker.git
```

Add your code to `suggestions.py` (in the `app` folder), so that the method `generate_suggestions` returns appropriate suggestions.


## Steps to build docker image:
```bash
docker build -t suggestor:v1 .
```

## Steps to run docker container
```bash
docker run -p 8080:8080 suggestor:v1
```

Access the API at `localhost:8080/get-suggestions/foo`
