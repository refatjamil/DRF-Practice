from rest_framework import serializers
from .models import StudentModel


def start_wirh_r(value):
    if value[0].lower() != 'r':
        raise serializers.ValidationError('Name should be start wirh r')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_wirh_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        return instance
    
    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full')
        return value
    
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        if nm.lower() == 'rafe' and ct.lower() != 'dhaka':
            raise serializers.ValidationError('City must be dhaka')
        return data