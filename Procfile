web: gunicorn training.wsgi
worker: celery worker -A training --queues=high,default --loglevel=INFO