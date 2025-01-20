FROM ubuntu:24.04

COPY main.py /main.py
COPY requirements.txt /requirements.txt

RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip && \
    python3 -m venv /venv && \
    /venv/bin/pip3 install --upgrade pip && \
    /venv/bin/pip3 install --upgrade setuptools && \
    /venv/bin/pip3 install -r /requirements.txt

EXPOSE 80/tcp

CMD ["/venv/bin/uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]  
