FROM python:3.12-slim

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY pyproject.toml /app/
RUN uv pip install -r pyproject.toml --system

COPY src/celery_trial/app.py src/celery_trial/celery_app.py src/celery_trial/tasks.py ./
CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]
