from django import forms
from django.forms import ModelForm
from user.models import User 


def checkpassword(password):
    l, u, p, d = 0, 0, 0, 0
    msg = ''
    s = '!@#$%^&*()_-+=*+-?><'
    for i in password:
        # counting lowercase alphabets
        if (i.islower()):
            l += 1

        # counting uppercase alphabets
        if (i.isupper()):
            u += 1

        # counting digits
        if (i.isdigit()):
            d += 1

        # counting the mentioned special characters
        if (i in s):
            p += 1
    if (l > 0 and u > 0 and p > 0 and d > 0 and l+p+u+d == len(password)):
        return True
    else:
        if(l<1 or u<1):
            msg = msg + 'password must contains lower and upper case alphabets'
        elif(d<1):
            msg = msg + 'password must contains digits'
        elif(p<1):
            msg = msg + 'password must contains special character'
        # else:
        #     msg = msg + 'password is not valid'
        return msg

class Registerform(ModelForm):
    first_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your first name','required':'True'}))
    last_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder':'Enter your last name','required':'True'}))
    email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email','required':'True'}))
    phone = forms.CharField(widget = forms.NumberInput(attrs={'placeholder' : 'phone number','required':'True'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************','required':'True'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'*************','required':'True'}))
    class Meta:
        model = User
        fields = ['first_name','last_name','phone','email','password','confirm_password']

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

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email).exists()
        if(user):
            raise forms.ValidationError('email is already exists')        
        return email
    
    def clean_password(self):
        password = self.cleaned_data['password']
        if(len(password)<8):
            raise forms.ValidationError('password must contain more than 8 character')
        else:
            if(checkpassword(password)==True):
                return password
            else:
                msg = checkpassword(password)
                raise forms.ValidationError(msg)
        
    
    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data and self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            msg = 'confirm password does not match'
            self.add_error('confirm_password',msg)
        return self.cleaned_data
        

    

# class Loginform(forms.Form):
#     email = forms.CharField(widget = forms.EmailInput(attrs={'placeholder':'Enter your email', 'name':'email'}))
#     password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'************','name':'password'}))
