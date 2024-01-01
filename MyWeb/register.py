from django.shortcuts import render
from django.http import HttpResponse
from .models import User  # Import your User model

def show_register(request):
    lang = request.GET.get('lang', 'en')

    if lang == 'en':
        file_view = 'register.html'
    else:
        file_view = 'register_cn.html'

    return render(request, file_view, {})

def do_register(request):
    lang = request.POST.get('lang', 'en')
    email = request.POST.get('email')
    name = request.POST.get('name')
    tel = request.POST.get('tel')
    company = request.POST.get('company')
    title = request.POST.get('title')
    password = request.POST.get('password')

    if not all([email, name, company, title, password]) or '@' not in email:
        error_msg = 'Please fill in the form correctly!' if lang == 'en' else '请按照规范填写表单'
        return render(request, f'register.html', {'error_msg': error_msg})

    try:
        # Create and save a new user using Django's ORM
        user = User(email=email, name=name, tel=tel, company=company, title=title, password=password)
        user.save()

        success_template = 'login.html' 
        return render(request, success_template, {})

    except Exception as e:
        # Handle exceptions, log the error, and return an appropriate response.
        return HttpResponse(f"Error: {e}")
