import os
from celery import Celery

# Задаём переменную окружения, содержащую название файла настроек нашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

app = Celery('myshop')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# Строчки добавленные с официальных доков по Celery:
@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
