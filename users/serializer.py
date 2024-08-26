from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username', 'first_name', 'last_name', 'email','profession', 'image','status','phone_number','address', 'bio','created']
        
class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True,write_only=True)
    phone_number=serializers.CharField()

    class Meta:
        model=User
        fields=['username', 'first_name', 'last_name', 'email', 'image', 'phone_number','profession', 'bio','address','password','confirm_password']
        
    def validate(self, data):
        if data['password']!=data['confirm_password']:
            raise serializers.ValidationError("Password do not match")
        if User.objects.filter(email=data['email']).exists():
             raise serializers.ValidationError("Email already Exist")
        if User.objects.filter(username=data['username']).exists():
             raise serializers.ValidationError("Username already Exist")
        return data
    def create(self, validated_data):
        user= User(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            image=validated_data['image'],
            bio=validated_data['bio'],
            phone_number=validated_data['phone_number'],
            address=validated_data['address'],
            profession=validated_data['profession']   
        )
        
        user.set_password(validated_data['password'])
        user.is_active=False
        user.save()
        return user
class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(required=True)
    password=serializers.CharField(required=True,write_only=True)
    class Meta:
        model=User
        fields=['email','password']

    