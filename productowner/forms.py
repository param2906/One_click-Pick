from django import forms
from django.forms import ModelForm
from user.models import User

class ProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','address','profile']
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha(): 
            raise forms.ValidationError('first name contains only alphabet') 
        return first_name
            
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        # for i in last_name:
        if not last_name.isalpha():
            raise forms.ValidationError('last name contains only alphabet')
        return last_name 
            
            
    def clean_phone(self):
        phone = self.cleaned_data['phone']
        print(phone)
        if(len(phone)==10):
            return phone 
        else:
            raise forms.ValidationError('phone number must be 10 digit')

    