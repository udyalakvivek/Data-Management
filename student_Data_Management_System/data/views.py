from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import registerForm, Add_Data_Form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Student_Data_Model


# Register Part 
def register(request):
    if request.method == 'POST':
        register_Form = registerForm(request.POST)
        if register_Form.is_valid():
            register_Form.save()
            register_Form = registerForm()
            messages.add_message(request, messages.SUCCESS, "Account Created Successfully!")
            return redirect('Login')
    else:
        register_Form = registerForm()
    return render(request,'registration/register.html',{'r_forms': register_Form})


# Login Part
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(request, username = name, password = pwd) 
            if user is not None:
                auth_login(request,user)
                messages.add_message(request, messages.SUCCESS, "You're logIn Successfully!")
                return redirect('Add_data') 
    else:
        form = AuthenticationForm()
    return render(request,'registration/login.html',{'l_forms':form})

# Logout Part 
def logout(request):
    auth_logout(request)
    return redirect('Show_data')

# View All Data 
def show_Student_Data(request):
    show_Data = Student_Data_Model.objects.all()
    return render(request,'show_Data.html',{'show_Data':show_Data})

# Add Data From UI
@login_required
def add_Student_Data(request):
    if request.method == 'POST':
        form_Data = Add_Data_Form(request.POST)
        if form_Data.is_valid():
            form_Data.save()
            form_Data = Add_Data_Form()
            return redirect('Show_data')
    else:
        form_Data = Add_Data_Form()
    return render(request,'add_Data.html',{'form_Data':form_Data})


# Edit Single person Data
@login_required
def edit_Student_Data(request,id):
    if request.method == 'POST':
        get_Data_Model = Student_Data_Model.objects.get(pk = id)
        edit_forms = Add_Data_Form(request.POST,instance=get_Data_Model)
        if edit_forms.is_valid():
            edit_forms.save()
            return redirect('Show_data')
    else:
        get_Data_Model = Student_Data_Model.objects.get(pk = id)
        edit_forms = Add_Data_Form(instance=get_Data_Model)
    return render(request,'update_Details.html',{'edit_forms':edit_forms})


# Delete Data 
@login_required
def delete_Student_Data(request,id):
    if request.method == 'POST':
        get_Data_Model = Student_Data_Model.objects.get(pk = id)
        get_Data_Model.delete()
        return redirect('Show_data')


# View Single Person Data
@login_required
def single_Person_Data(request,id):
    view_Data = get_object_or_404(Student_Data_Model,pk=id)
    return render(request,'view_Single_Data.html',{'view_Data':view_Data})