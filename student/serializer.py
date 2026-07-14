from rest_framework import serializers
from .models import Student,Admin

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
    
    def validate_name(self,name):
        if not name.isalpha():
            raise ValueError('enter the name correctly')
        else:
            return name
        

    def validate_rollno(self,rollno):
        if not rollno.isdigit():
            raise ValueError('enter the rollno correctly')
        else:
            return rollno
        
class AminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'
        
    
    def validate_name(self,name):
        if not name.isalpha():
            raise ValueError('enter the name correctly')
        else:
            return name
        

    def validate_username(self,username):
        if not username.endswith('@gmail.com'):
            raise ValueError('username ends with @gmail.com')
        else:
            return username