from .celery import app as celery_app


# Добавлена строчка из официальных доков по Celery:
__all__ = ('celery_app',)
