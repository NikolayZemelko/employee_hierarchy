from rest_framework import serializers
from .models import Employee


class SupervisorSerializer(serializers.ModelSerializer):

    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Employee
        fields = ("id", "full_name")


class EmployeeSerializer(serializers.ModelSerializer):
    supervisor = SupervisorSerializer(many=False, read_only=True)
    photo = serializers.ImageField()
    full_name = serializers.SerializerMethodField()
    job_title = serializers.SerializerMethodField()

    def get_job_title(self, obj):
        return obj.get_job_title_display()

    def get_full_name(self, obj):
        return obj.__str__()

    class Meta:
        model = Employee
        exclude = ("date_created",)
