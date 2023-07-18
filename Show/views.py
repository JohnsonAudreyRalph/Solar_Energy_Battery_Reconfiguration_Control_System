from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import requests

# Create your views here.
# def Login(req):
#     return render(req, 'login.html')

class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        if request.method == "POST":
            username = request.POST.get('User_Name')
            Password = request.POST.get('Password')
            user = authenticate(username=username, password=Password)
            if user is not None:
                # Kiểm tra điều kiện hợp lệ ==> Đăng nhập thành công
                login(request, user)
                return redirect('/Login_Success')
            else:
                try:
                    # Kiểm tra điều kiện tên người dùng nhập vào có tồn tại hay không
                    User.objects.get(username=username)
                    # Nếu người dùng có tồn tại, nhưng mật khẩu sai ==> Reload lại trang web để người dùng đăng nhập lại
                    messages.error(request, "Sai thông tin đăng nhập!!!!")
                    return redirect('/')
                except User.DoesNotExist:
                    messages.error(request, "Không tồn tại tài khoản này")
                    return redirect('/')

class Affter_Login(View):
    def get(self, request):
        url = "http://solar-ctd.ddns.net/data/line"
        response = requests.get(url)
        data = response.json()

        line1_power = data["data"]["line1"]["power"]
        line1_volt = data["data"]["line1"]['volt']
        line1_perform = data["data"]["line1"]["perform"]
        line1_ampe = data["data"]["line1"]["ampe"]

        line2_power = data["data"]["line2"]["power"]
        line2_volt = data["data"]["line2"]['volt']
        line2_perform = data["data"]["line2"]["perform"]
        line2_ampe = data["data"]["line2"]["ampe"]

        conx = {
            'line1_power':line1_power,
            'line1_volt':line1_volt,
            'line1_perform':line1_perform,
            'line1_ampe':line1_ampe,
            'line2_power':line2_power,
            'line2_volt':line2_volt,
            'line2_perform':line2_perform,
            'line2_ampe':line2_ampe
        }

        return render(request, 'index.html', conx)
    
def Logout(request):
    logout(request)
    messages.error(request, "Bạn đã đăng xuất")
    return redirect('/')

def index_HTML(req):
    return render(req, 'index.html')

def solars_HTML(req):
    return render(req, 'solars.html')

def configuration_HTML(req):
    return render(req, 'configuration.html')

def changepass_HTML(request):
    context = {}
    if request.method=='POST':
        pass_old = request.POST['pass_old']
        pass_new  = request.POST['pass_new']
        user = User.objects.get(id=request.user.id)
        check = user.check_password(pass_old)
        print(check)
        if check==True:
            user.set_password(pass_new)
            user.save()
            context['mess'] = 'Thay đổi mật khẩu thành công!!!'
            context['error'] = 'success_mess'
        else:
            context['mess'] = 'Mật khẩu bạn nhập không đúng'
            context['error'] = 'error_mess'


    return render(request, 'changepass.html', context)