# Sample Flask Docker API

## Steps to build docker image:
```bash
docker build -t suggestor:v1 .
```

## Steps to run docker container
```bash
docker run -p 8080:8080 suggestor:v1
```

Access the API at `localhost:8080/get-suggestions/foo`
