from celery import Celery

celery_app = Celery(
    "celery_worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
    include=["tasks"],
)
