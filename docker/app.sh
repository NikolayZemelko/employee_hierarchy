#!/bin/bash

make migrate
make seed
gunicorn -b=0.0.0.0:8000 employee_hierarchy.wsgi:application --workers 4
