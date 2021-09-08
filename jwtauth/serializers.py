# jwtauth/serializers.py
from database.models import User
from rest_framework import serializers


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, label="Confirm password")
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "firstname",
            
            "lastname",
            "is_patient",
            "is_dentist",
            "is_clinic",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        
        is_dentist = validated_data["is_dentist"]
     
        firstname = validated_data["firstname"]
        lastname = validated_data["lastname"]
        
        is_clinic = validated_data["is_clinic"]
        is_patient = validated_data["is_patient"]
        
        if (email and User.objects.filter(email=email).exclude(username=username).exists()):
            raise serializers.ValidationError(
                {"email": "Email addresses must be unique."})
        if password != password2:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})
        user = User(username=username, email=email, firstname=firstname, lastname=lastname,is_dentist=is_dentist,is_patient=is_patient, is_clinic=is_clinic)
        user.set_password(password)
        user.save()
        return user