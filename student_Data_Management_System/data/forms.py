from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth.models import User
from .models import Student_Data_Model

class registerForm(UserCreationForm):
    # usable_password = None
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm','placeholder' : "Enter Password" }),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm','placeholder' : "Confirm Password"}),label=' Confirm Password')
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm','placeholder' : "Enter Your Username"}),label='UserName')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm','placeholder' : "Enter Your Email"}),label='Email')
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


class Add_Data_Form(forms.ModelForm):
    class Meta:
        model = Student_Data_Model
        fields = '__all__'
        widgets = {
           'name' : forms.TextInput(attrs={
               'class' : 'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm',
               'placeholder': 'Enter Your Name',
           }),
           'father_name' : forms.TextInput(attrs={
               'class' : 'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm',
               'placeholder': 'Enter Father Name'
           }),
           'mother_name' : forms.TextInput(attrs={
               'class' : 'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm',
               'placeholder': 'Enter Mother Name'
           }),
           'email' : forms.EmailInput(attrs={
               'class' : 'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm',
               'placeholder': 'Enter Your Gmail'
           }),
           'roll_number' : forms.TextInput(attrs={
               'class' : 'w-full px-5 py-1 text-orange-600 border-2 rounded-md shadow-sm focus:outline-none focus:ring-orange-600 focus:border-orange-600 sm:text-sm',
               'placeholder': 'Enter Your RollNo.'
           }),
        }