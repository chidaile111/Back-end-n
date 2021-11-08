from django.shortcuts import redirect, render
import datetime
from nguoidung.forms import CreateNewUser
from icecream import ic

#Create your views here.

def home_view(request):
    return render(
        request,
        'Meeting Chat/index.html',
        # 'Homepage/UserHomepage.html',
        {
            'now': datetime.datetime.now()
        }
    )
def create_new_user_view(request):
    if request.method == 'POST':
        form= CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CreateNewUser
    return render(
        request,
        # 'Homepage/UserHomepage.html',
        'dangki.html',
        {
            'form': form
        }
    )
    
# def login(request):
#     if re