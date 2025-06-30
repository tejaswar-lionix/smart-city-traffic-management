build:
	docker build -t smart-city-traffic .
	pip install -r requirements.txt
	npm install

test:
	pytest -q
	npm test

run:
	python manage.py runserver 0.0.0.0:8000
