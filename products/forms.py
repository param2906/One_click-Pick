from django import forms
from django.forms import ModelForm
from products.models import Products
from products.models import Category,Section,Colour,Size

class ProductForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter product name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    company = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter company  name",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    size = forms.ModelMultipleChoiceField(queryset=Size.objects.all(),help_text = 'Hold down “Control”, or “Command” on a Mac, to select more than one.',
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
            }
        )
    )
    price = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter price",
                "data-validation-required-message": "Please enter product price",
            }
        )
    )
    inventory = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter the number of items in stock",
                "data-validation-required-message": "Please enter product price",
            }
        )
    )
    colour = forms.ModelMultipleChoiceField(queryset=Colour.objects.all(),help_text = 'Hold down “Control”, or “Command” on a Mac, to select more than one.',
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                # "placeholder": "Enter colour",
            }
        )
    )
    section = forms.ModelChoiceField(queryset=Section.objects.all(), empty_label="Select section",required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control form-select mb-3",
                "required": "True",
            }
        )
    )
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Select category",required=False,
        widget=forms.Select(
            attrs={
                "class": "form-control form-select mb-3",
                "required": "True",
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                # "multiple":"True",
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class": "form-control mb-3",
                "required": "True",
                "placeholder": "Enter Description Here",
                "data-validation-required-message": "Please enter your name",
            }
        )
    )
    # created_by = forms.CharField(
    #     widget=forms.TextInput(
    #     attrs={
    #         "class": "form-control mb-3",
    #         "required": "True",
    #         "data-validation-required-message": "Please enter your name",
    #         "disabled":"True",
    #     }
    #     )
    # )
    class Meta:
        model = Products
        fields = [
            "name",
            "company",
            "size",
            "price",
            "inventory",
            "colour",
            "section",
            "category",
            "image",
            # "multipleimage",
            "description",
            # "created_by",
        ]

    def clean_name(self):
        name = self.cleaned_data['name']
        s = '!@#$%^&*()_-+=*+-?><'
        
        if  name in s: 
            raise forms.ValidationError('names must contain character')
        return name 
        

    

