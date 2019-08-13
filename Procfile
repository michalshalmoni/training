web: gunicorn training.wsgi
worker: celery -A training worker --concurrency=8 --loglevel=info