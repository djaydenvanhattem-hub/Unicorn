# id="backend_docker_v63"
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy psycopg2-binary redis python-jose

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
