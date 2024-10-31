import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

BROKER_URL = os.getenv('BROKER_URL', 'amqp://jaotarzan:Batata_12@localhost:5672/fabricahistologia')

app = Celery('django_project', broker=BROKER_URL)

app.conf.update(
    broker_connection_retry_on_startup=True,
)

app.conf.task_always_eager = False

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')