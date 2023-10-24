FROM tiangolo/uvicorn-gunicorn:python3.10

COPY . /app

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
