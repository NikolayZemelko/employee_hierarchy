from rest_framework import serializers
from .models import Employee


class SupervisorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, supervisor):
        return f'{supervisor.first_name} {supervisor.last_name}'

    class Meta:
        model = Employee
        exclude = ['date_created']


class EmployeeSerializer(serializers.ModelSerializer):
    supervisor = SupervisorSerializer(required=False)
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, employee):
        return f'{employee.first_name} {employee.last_name}'

    class Meta:
        model = Employee
        exclude = ['date_created']
