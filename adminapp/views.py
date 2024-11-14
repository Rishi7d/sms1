import calendar
import random
import string

from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, get_object_or_404

def projecthomepage(request):
    return render(request,'adminapp/ProjectHomePage.html')

def printpagecall(request):
    return render(request,'adminapp/printer.html')

def printpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'User input: {user_input}')
    a1= {'user_input':user_input}
    return render(request,'adminapp/printer.html',a1)

def exceptionpagecall(request):
    return render(request, 'adminapp/ExceptionExample.html')

def exceptionpagelogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        result = None
        error_message = None
        try:
            num = int(user_input)
            result = 10 / num
        except Exception as e:
            error_message = str(e)
        return render(request, 'adminapp/ExceptionExample.html', {'result': result, 'error': error_message})
    return render(request, 'adminapp/ExceptionExample.html')

def randompagecall(request):
    return render(request, 'adminapp/randomexample.html')

def randompagelogic(requset):
    if requset.method == 'POST':
        number1=int(requset.POST['number1'])
        ran = ''.join(random.sample(string.ascii_uppercase + string.digits,k=number1))
    a1={'ran':ran}
    return render(requset,'adminapp/randomexample.html',a1)

def calculatorpagecall(request):
    return render(request, 'adminapp/calculator.html')

def calculatorpagelogic(request):
    result = None
    if request.method == 'POST':
        num1 = float(request.POST.get('num1'))
        num2 = float(request.POST.get('num2'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else 'Infinity'

    return render(request, 'adminapp/calculator.html', {'result': result})

def datetimepagecall(request):
    return render(request, 'adminapp/datetimepage.html')

import datetime
import calendar
import time
from datetime import timedelta
def datetimepagelogic(request):
    if request.method == "POST":
        number1 = int(request.POST['date1'])
        x = datetime.datetime.now();
        ran=x + timedelta(days=number1)
        ran1 = ran.year
        ran2 = calendar.isleap(ran1)
        if ran2 == False:
            ran3 = "Not leap year"
        else:
            ran3 = "Leap year"
    a1 = {'ran':ran, 'ran3':ran3, 'ran1':ran1, 'number1':number1}
    return render(request, 'adminapp/datetimepage.html', a1)

from .models import Task
from .forms import TaskForm

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_task')
    else:
        form = TaskForm()
    tasks = Task.objects.all()
    return render(request, 'adminapp/add_task.html',
                  {'form': form, 'tasks': tasks})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('add_task')

from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
def UserRegisterPageCall(request):
    return render(request, 'adminapp/UserRegisterPage.html')
def UserRegisterPageLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/UserRegisterPage.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/UserRegisterPage.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projecthomepage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/UserRegisterPage.html')
    else:
        return render(request, 'adminapp/UserRegisterPage.html')

def UserLoginPageCall(request):
    return render(request, 'adminapp/UserLoginPage.html')

def UserLoginPageLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if len(username) == 10:
                # Redirect to StudentHomePage
                messages.success(request, 'Login successful as student!')
                return redirect('studentapp:StudentHomePage')
                # return render(request, 'studentapp/StudentHomepage.html')
            elif len(username) == 4:
                # Redirect to FacultyHomePage
                # messages.success(request, 'Login successful as faculty!')
                return redirect('facultyapp:FacultyHomePage')
                # return render(request, 'facultyapp/FacultyHomepage.html')
            else:
                # Invalid username length
                messages.error(request, 'Username length does not match student or faculty criteria.')
                return render(request, 'adminapp/UserLoginPage.html')
        else:
            # If authentication fails
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/UserLoginPage.html')
    else:
        return render(request, 'adminapp/UserLoginPage.html')

def logout(request):
    auth.logout(request)
    return redirect('projecthomepage')

from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'adminapp/confirmation.html')
    else:
        form = FeedbackForm()
    return render(request, 'adminapp/feedback_form.html', {'form': form})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail

def contact_list(request):
    contacts = Contact.objects.all()
    query = request.GET.get('q')
    if query:
        contacts = contacts.filter(name__icontains=query) | contacts.filter(email__icontains=query)
    return render(request, 'adminapp/contact_list.html', {'contacts': contacts})

def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            email = request.POST.get('send_email')
            if email:
                send_mail(
                    'New Contact Details',
                    f'Name: {contact.name}\nEmail: {contact.email}\nPhone: {contact.phone}\nAddress: {contact.address}',
                    'rishiraja118@gmail.com',
                    [email],
                )
            return redirect('contact_list')
    else:
        form = ContactForm()
    return render(request, 'adminapp/add_contact.html', {'form': form})

def delete_contact(request, pk):
    contact = Contact.objects.get(pk=pk)
    contact.delete()
    return redirect('contact_list')