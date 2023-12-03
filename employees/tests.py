from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Employee


class EmployeesTestCase(TestCase):

    fixtures = ["employees.json"]

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            first_name="Nikolay",
            last_name="Zemelko",
            password="Kola1989"
        )
        # Create some employees for testing
        self.all_employees = Employee.objects.count()
        self.employee1 = Employee.objects.get(pk=1)
        self.employee2 = Employee.objects.get(pk=2)
        self.employee3 = Employee.objects.get(pk=3)
        self.employee4 = Employee.objects.get(pk=4)
        self.employee5 = Employee.objects.get(pk=5)


class EmployeeListViewTestCase(EmployeesTestCase):

    def test_employees_view(self):
        self.client.force_login(self.user)
        self.url = reverse('employees-index')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employees_index.html')
        self.assertContains(response, self.employee1.first_name)
        self.assertContains(response, self.employee2.first_name)


class EmployeeDetailViewTestCase(EmployeesTestCase):

    def test_employee_detail_view(self):
        self.client.force_login(self.user)
        self.url = reverse('employee-detail', kwargs={"pk": 3})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'employees/employee_detail.html')
        self.assertContains(response, self.employee3.first_name)

    def test_employee_detail_no_login_view(self):
        self.url = reverse('employee-detail', kwargs={"pk": 3})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)


class EmployeeDeleteViewTestCase(EmployeesTestCase):

    def test_employee_delete_view(self):
        self.client.force_login(self.user)
        self.url = reverse('employee-delete', kwargs={"pk": 3})
        self.client.post(self.url)
        self.url = reverse('employees-index')
        response = self.client.get(self.url)
        self.assertEqual(self.all_employees - 1, response.context['employees'].count())

    def test_employee_delete_no_login_view(self):
        self.url = reverse('employee-delete', kwargs={"pk": 3})
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
