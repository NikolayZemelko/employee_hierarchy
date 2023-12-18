from rest_framework import serializers
from .models import Employee


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ("date_created",)


class EmployeeSerializer(serializers.ModelSerializer):
    supervisor = SupervisorSerializer(many=False, read_only=True)

    class Meta:
        model = Employee
        exclude = ("date_created",)
