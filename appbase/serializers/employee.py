from rest_framework import serializers
from ..models.employee import Employee

class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model=Employee
        fields='__All__'