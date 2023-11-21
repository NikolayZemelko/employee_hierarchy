MANAGE := python3 manage.py

seed:
	$(MANAGE) flush --no-input
	$(MANAGE) seed employees --number=1 --seeder "Employee.id" 1 --seeder "Employee.job_title" "SR" --seeder "Employee.salary" 300000
	$(MANAGE) seed employees --number=50 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "MD" --seeder "Employee.salary" 150000
	$(MANAGE) seed employees --number=40950 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "JR" --seeder "Employee.salary" 60000

seed-render:
	$(MANAGE) flush --no-input
	$(MANAGE) seed employees --number=1 --seeder "Employee.id" 1 --seeder "Employee.job_title" "SR" --seeder "Employee.salary" 300000
	$(MANAGE) seed employees --number=10 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "MD" --seeder "Employee.salary" 150000
	$(MANAGE) seed employees --number=30 --seeder "Employee.supervisor_id" 3 --seeder "Employee.job_title" "JR" --seeder "Employee.salary" 60000

lint:
	flake8 .

test:
	$(MANAGE) test

dev:
	$(MANAGE) runserver

docker-start:
	poetry run pip freeze > requirements.txt
	docker-compose build --no-cache
	docker-compose up


shell:
	$(MANAGE) shell_plus --print-sql

# Database commands
migrations:
	$(MANAGE) makemigrations

check_before_migrate:
	$(MANAGE) check

migrate:
	$(MANAGE) migrate
