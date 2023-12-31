from django.shortcuts import render, redirect
from app01 import models


# Create your views here.
def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    user_ob = models.UserInfo.objects.filter(username=user, password=pwd).first()
    if user_ob:
        request.session['user_id'] = {"name": user_ob.username, "id": user_ob.id}
        return redirect('/home/')
    else:
        return render(request, 'login.html', {'error': '用户名或密码错误'})


def home(request):
    info_dict = request.info_dict
    return render(request, 'home.html')
