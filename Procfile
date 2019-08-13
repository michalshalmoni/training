web: gunicorn training.wsgi
worker: celery worker -A --app=training --queues=high,default --loglevel=INFO