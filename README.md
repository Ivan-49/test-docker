docker build -t test-fastapi-6 .
docker run --rm -it -p 8000:8000/tcp test-fastapi-6:latest