web: gunicorn training.wsgi
worker: celery -A training worker --concurrency=3 --loglevel=info