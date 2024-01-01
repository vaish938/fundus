# login.py

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User  # Import your User model

def homePage(request):
    file_view = 'homepage.html'
    return render(request, file_view, {})

def login(request):
    # already login
    if request.session.get('username', None) is not None:
        return HttpResponseRedirect('/uploadfile')

    # homepage.html <a href="/login?lang=en">
    if request.method == 'GET':
        lang = request.GET.get('lang', 'en')

        if lang == 'en':
            file_view = 'login.html'
        else:
            file_view = 'login_cn.html'
        return render(request, file_view, {})
    else:
        # login validation
        lang = request.POST.get('lang', 'en')

        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=username, password=password)

            # Set session variables
            request.session['username'] = user.email
            request.session['lang'] = lang
            # Additional session variables if needed
            # request.session['softmax_or_sigmoids'] = my_config.SOFTMAX_OR_SIGMOIDS

            if lang == 'en':
                file_view = 'uploadfile.html'
            else:
                file_view = 'uploadfile_cn.html'
            return render(request, file_view, {})

        except User.DoesNotExist:
            # login failure
            if lang == 'en':
                return render(request, 'login.html', {'err_msg': 'Email or password error!'})
            else:
                return render(request, 'login_cn.html', {'err_msg': '邮箱或者密码错误!'})

def register(request):
    lang = request.POST.get('lang', 'en')

    if lang == 'en':
        file_view = 'register.html'
    else:
        file_view = 'register_cn.html'
    return render(request, file_view, {})
def show_upload(request):
    
    # do not login
    if request.session.get('username', None) is None:
        return render(request, 'homepage.html')

    # 显示上传图像页面
    lang =request.session.get('lang')
    if lang == 'en':
        # 英文版
        file_view = 'uploadfile.html'
    else:
        # 中文版
        file_view = 'uploadfile_cn.html'
    return render(request, file_view, {})
def logout(request):
    del request.session['username']
    del request.session['lang']

    return render(request, 'homepage.html', {})
