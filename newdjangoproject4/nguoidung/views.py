from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
import datetime
# from nguoidung.forms import CreateNewUser
from icecream import ic
#from newdjangoproject4.nguoidung.models import thongtinnguoidung
from nguoidung.forms import TaoNguoiDungMoi
from nguoidung.forms import DangKy
from django.contrib.auth import login, authenticate

# Create your views here.

def homepage_view(request):
    return render(
        request,
        'Meeting Chat/index.html',
        {
            'now': datetime.datetime.now(),
        }
    )
    
def userhomepage_view(request):
    return render(
        request,
        'Homepage/UserHomepage.html',
        {
            'now': datetime.datetime.now(),
            #'user': User,
        }
    )



def dangky(request):
    if request.method == 'POST':
        form1 = DangKy(request.POST)
        form2 = TaoNguoiDungMoi(request.POST)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('/dang_nhap')
    else:
        form1 = DangKy()
        form2 = TaoNguoiDungMoi()
    return render(
        request,
        'dangky.html',
        {
            'form1': form1,
            'form2': form2
        }   
    )
    