from rest_framework import serializers
from .models import *
from datetime import datetime

# class UserSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True)
#     class Meta:
#         model = User
#         fields = ['email','password', 'groups']
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name', 'date_joined')

    def create(self, validated_data):
        # Hash the password before saving the user
        password = validated_data.pop('password')  # Get the password
        hashed_password = make_password(password)  # Hash the password
        user = User.objects.create(**validated_data, password=hashed_password)  # Create the user with hashed password
        return user

    # def validate_password(self, value):
    #     try:
    #         validate_password(value)
    #     except ValidationError as e:
    #         raise serializers.ValidationError(e.messages)
    #     return value

    # def create(self, validated_data):
    #     return User.objects.create_user(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class ProjectsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['owner'] = instance.owner.email if instance.owner else None
        return representation
    class Meta:
        model = Projects
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'status', 'priority', 'due_date')

class TaskDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['project'] = instance.project.name if instance.project else None
        return representation
    def validate_due_date(self, value):
        if value <= datetime.now().date():
            raise serializers.ValidationError("The due date cannot be in the past.")
        return value
    class Meta:
        model = Tasks
        fields = '__all__'
        
        
class CommentsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email if instance.user else None
        representation['task'] = instance.task.title if instance.task else None
        return representation
    class Meta:
        model = Comments
        fields = '__all__'
        
class CommentsDetailSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email if instance.user else None
        representation['task'] = instance.task.title if instance.task else None
        return representation
    class Meta:
        model=Comments
        fields='__all__'