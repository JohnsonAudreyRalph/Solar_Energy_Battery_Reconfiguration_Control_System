from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
        return render(request, 'index.html')
    
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