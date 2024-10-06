from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    # Validators
    def start_with_y(self, value):
        if value[0].lower() != 'y':
            raise serializers.ValidationError('Name should start with Y')  # Fix the error message to match the validator
    
    name = serializers.CharField(validators=[start_with_y])
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
        read_only_fields = ['name', 'city']
    
    # Field-Level Validation
    def validate_roll(self, value):
        if value >= 100:
            raise serializers.ValidationError('Roll should be between 1 and 100')
        return value
    
    # Object-Level Validation
    def validate(self, attrs):
        nm = attrs.get('name')
        ct = attrs.get('city')
        if nm.lower() == 'oscar piastri' and ct.lower() != 'melbourne':
            raise serializers.ValidationError('City must be Melbourne if the name is Oscar Piastri')
        return attrs
