FROM python:3.11-slim

WORKDIR /project

COPY backend/requirements.txt backend/
RUN pip install --default-timeout=100 --no-cache-dir -r backend/requirements.txt

COPY . .

ENV PYTHONPATH=/project

CMD ["uvicorn", "backend.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
