from rest_framework import serializers
from .models import UserModel
import string

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'


    def validate_email(self, data):
        obj = UserModel.objects.filter(email=data)
        if obj:
            raise serializers.ValidationError('email must be unique')
        return data

    def validate(self, attrs):
        if "username" in attrs:
            if " " in attrs['username']:
                raise serializers.ValidationError("username must not contain special characters except '.','_'")
            for i in string.punctuation:
                if (i != ".") and (i != "_"):
                    if i in attrs['username']:
                        raise serializers.ValidationError("username must not contain special characters except '.','_'")
        return attrs

