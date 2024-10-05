from rest_framework import serializers
from .models import Student

#Validators
def start_with_y(value):
    if value[0].lower() != 'y':
        raise serializers.ValidationError('Name should start with R')


class StudentSerializer(serializers.Serializer):
    
    name = serializers.CharField(max_length=100, validators = [start_with_y])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        # print(instance.name)
        instance.name = validated_data.get('name', instance.name)
        # print(instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
    
    # Field Level Validation
    def  validate_roll(self, value):
        if value >=100:
            raise serializers.ValidationError('Roll should be between 1 to 100')
        return value
    
    #Object Level Validation
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower()=='oscar piastri' and ct.lower()!='melbourne':
            raise serializers.ValidationError('City must be Melbourne')
        return data
            

