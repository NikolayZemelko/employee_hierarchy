from django.contrib.auth.models import User
from django.db import models


class Employee(User):

    job_title = models.CharField(max_length=50)
    date_offered = models.DateField()
    salary = models.IntegerField()
    supervisor = models.ForeignKey('self',
                                   on_delete=models.SET_NULL,
                                   related_name='employees',
                                   related_query_name='supervisor',
                                   )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
