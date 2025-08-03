lint:
	uv run ruff check --fix

start:
	uv run manage.py runserver