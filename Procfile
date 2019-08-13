web: gunicorn training.wsgi
worker: celery worker -A training.tasks worker --concurrency=1 --loglevel=info