1. Необходимо в settings.py указать действительный почтовый адрес и пароль (EMAIL_HOST_USER и EMAIL_HOST_PASSWORD).
2. Запустить celery -A send_email worker -l info
3. Запустить celery -A send_email beat -l info

Официальная документация celery для настройки переодических задач:
https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html?highlight=period
