## what is this?
This is a web app simple toy.
fastapi/docker/typescript/dynamodb

## how to use


## to do
- [×] make api using fast api
- [×] make api using fast api on docker
- [ ] deploy on lambda


## note
post method usage from curl

```
curl -X 'POST' 'http://127.0.0.1:8000/save_person' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"name": "op", "age": 60}'
```

docker build and run

```
$ cd /Path/to/webapp_toy/backend
$ docker build -t myfastapiapp .
$ docker run -v /Path/to/webapp_toy/backend/data:/app/data -d --name myfastapiapp_container -p 8000:8000 myfastapiapp
```