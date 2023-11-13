from faker import Faker
from employees.models import Employee


def dataloader():
    Faker.seed(0)
    fake = Faker()

    for i in range(50000):
        Employee.objects.create()


