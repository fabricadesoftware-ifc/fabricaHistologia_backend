web: gunicorn --pythonpath src django_project.wsgi:application
worker: python -m celery --workdir src -A django_project worker --loglevel=info