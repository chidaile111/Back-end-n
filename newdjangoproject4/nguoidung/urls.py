from django.urls import path
from nguoidung import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.homepage_view, name='homepage'),
    path('dang_ky/', views.dangky, name='dangky'),
    path('home/', views.userhomepage_view, name='userhome'),
    path('dang_nhap/', auth_views.LoginView.as_view(template_name="dangnhap.html"), name='dangnhap'),
    
]
urlpatterns += staticfiles_urlpatterns()