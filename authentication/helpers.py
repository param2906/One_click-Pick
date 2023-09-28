from django.core.mail import send_mail
import uuid
from django.conf import settings

def send_verification_otp(email,otp):
    subject = 'Your OTP'
    message = f'your OTP number is - {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True

def send_forget_password_email(email,token):
    subject = 'Your forget password link'
    message = f'Hi click on the link to restet your password -http://127.0.0.1:8000/account/changepassword/{token}/'
    email_from = settings.EMAIL_HOST_USER 
    recipient_list = [email]
    send_mail(subject,message,email_from,recipient_list)
    return True