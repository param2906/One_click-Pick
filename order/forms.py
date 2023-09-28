from django import forms
from django.forms import ModelForm
from order.models import Order

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ["first_name","last_name","phone","email","address1","address2"]   

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
        if(len(phone)==10):
            return phone 
        else:
            raise forms.ValidationError('phone number must be 10 digit')
        
    def clean_address1(self):
        address1 = self.cleaned_data['address1']   
        if(len(address1)>5):
            return address1 
        else:
            raise forms.ValidationError('Enter the proper address')
        
    def clean_address2(self):
        address2 = self.cleaned_data['address2']   
        if(len(address2)>5):
            return address2
        else:
            raise forms.ValidationError('Enter the proper address')