lint:
	uv run ruff check --fix

start:
	uv run manage.py runserver

migrations:
	uv run manage.py makemigrations
	uv run manage.py migrate