web: gunicorn training.wsgi
worker: celery worker -A --app=training -l INFO