1. Необходимо в settings.py указать действительный почтовый адрес и пароль (EMAIL_HOST_USER и EMAIL_HOST_PASSWORD).
2. Выполнить команду 
   celery -A send_email worker -l info