MANAGE := python manage.py

lint:
	flake8 .

dev:
	$(MANAGE) runserver

shell:
	$(MANAGE) shell_plus --print-sql

# Database commands
migrations:
	$(MANAGE) makemigrations

check_before_migrate:
	$(MANAGE) check

migrate:
	$(MANAGE) migrate
