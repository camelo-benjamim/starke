from django.contrib.auth import forms
from accounts.models import Account
from django.forms import ModelForm

from django.contrib.auth import admin as adm

class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = Account
        fields = ("name","email",'phone','date_of_birth',"password1","password2")
        labels = {"name":("Nome: "),'email':("Email: "),'phone':("Phone: "),'date_of_birth':("Data de nascimento: ")}
class UserChangeForm(forms.UserChangeForm):
    password = forms.ReadOnlyPasswordHashField()
    class Meta(forms.UserChangeForm.Meta):
        model = Account
        fields = ("name","email",'phone','date_of_birth')
        labels = {"name":("Nome: "),'email':("Email: "),'phone':("Phone: "),'date_of_birth':("Data de nascimento: ")}
        def clean_password(self):
            return self.initial["password"]
   
    

class UserDeleteForm(ModelForm):
    class Meta:
        model = Account
        fields = ['email']