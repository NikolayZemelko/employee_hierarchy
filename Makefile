MANAGE := python3 manage.py
POETRY := poetry run

install:
	poetry install

seed-first:
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=1 --seeder "Employee.id" 1 --seeder "Employee.job_title" "CEO" --seeder "Employee.salary" 900000 --seeder "Employee.supervisor_id" 1

flush-dev:
	$(MANAGE) flush --no-input --settings=employee_hierarchy.settings-dev

seed-dev:
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=10 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "SR" --seeder "Employee.salary" 300000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=50 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "MD" --seeder "Employee.salary" 150000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=200 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "JR" --seeder "Employee.salary" 60000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=300 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "IN" --seeder "Employee.salary" 50000

seed-render:
	$(MANAGE) flush --no-input
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=1 --seeder "Employee.id" 1 --seeder "Employee.job_title" "CEO" --seeder "Employee.salary" 900000 --seeder "Employee.supervisor_id" 1
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=10 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "SR" --seeder "Employee.salary" 300000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=50 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "MD" --seeder "Employee.salary" 150000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=200 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "JR" --seeder "Employee.salary" 60000
	$(MANAGE) seed employees --settings employee_hierarchy.settings-dev --number=300 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "IN" --seeder "Employee.salary" 50000

lint:
	$(POETRY) flake8 .

test:
	$(POETRY) $(MANAGE) test --no-input

test-coverage:
	$(POETRY) coverage run manage.py test
	$(POETRY) coverage report -m --include=employees/* --omit=settings.py
	$(POETRY) coverage xml --include=employees/* --omit=settings.py

dev:
	$(POETRY) $(MANAGE) runserver --settings employee_hierarchy.settings-dev

PORT ?= 8000
start:
	$(POETRY) gunicorn -b=0.0.0.0:$(PORT) employee_hierarchy.wsgi:application --workers 4

docker-start:
	$(POETRY) pip freeze > requirements.txt
	docker-compose build --no-cache
	docker-compose up

shell:
	$(POETRY) $(MANAGE) shell_plus --print-sql
# Database commands
migrations:
	$(MANAGE) makemigrations

check_before_migrate:
	$(MANAGE) check

migrate:
	$(MANAGE) migrate
	$(MANAGE) migrate --settings=employee_hierarchy.settings-dev
