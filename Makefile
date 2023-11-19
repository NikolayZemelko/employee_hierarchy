MANAGE := python3 manage.py

seed:
	$(MANAGE) seed employees --number=1 --seeder "Employee.id" 1 --seeder "Employee.job_title" "Senior" --seeder "Employee.salary" 300000
	$(MANAGE) seed employees --number=50 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "Middle" --seeder "Employee.salary" 150000
	$(MANAGE) seed employees --number=40950 --seeder "Employee.supervisor_id" 1 --seeder "Employee.job_title" "Junior" --seeder "Employee.salary" 60000

lint:
	flake8 .

test:
	$(MANAGE) test

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
