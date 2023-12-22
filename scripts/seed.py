import argparse
import os
import random

from django_seeder import Seed

from employees.models import Employee
from django.conf import settings


SEEDS_COUNT = {
    'DEV': {
        'SR': 1,
        'MD': 50,
        'JR': 100
    }
}


def run():
    # parser = argparse.ArgumentParser(description="Choose your seeder.")
    # parser.add_argument('-f', '--format')
    # parser.add_argument('env', metavar='type of environment')
    # args = parser.parse_args()
    # ENV = args.env

    amount_of_seeds = SEEDS_COUNT.get("DEV")
    if settings.DEBUG:
        Employee.objects.all().delete()
    seeder = Seed.seeder()

    """Add Senior employees"""
    seeder.add_entity(Employee, amount_of_seeds['SR'], {
        'id': 1,
        'supervisor_id': None,
        'job_title': 'SR',
        'salary': 600000,
        'photo': None
    })
    seeder.execute()
    """Add Middle employees"""
    seeder.add_entity(Employee, amount_of_seeds['MD'], {
        'job_title': 'MD',
        'supervisor_id': 1,
        'salary': random.randint(150000, 250000),
        'photo': None
    })
    seeder.execute()
    """Add Junior employees"""
    seeder.add_entity(Employee, amount_of_seeds['JR'], {
        'job_title': 'JR',
        'supervisor_id': 1,
        'salary': random.randint(150000, 250000),
        'photo': None
    })

    seeder.execute()
