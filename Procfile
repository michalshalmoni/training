web: gunicorn training.wsgi
worker: celery -A training worker --concurrency=1 --loglevel=info
beat: celery -A training beat