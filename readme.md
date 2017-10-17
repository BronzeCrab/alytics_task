# Как запустить:
	- pip3 install -r requirements.txt
	- sudo apt-get install rabbitmq-server
	- sudo rabbitmq-server start
	- celery -A alytics_task worker --loglevel=info
	- python3 manage.py runserver
