from django.urls import path
from nguoidung import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-new-user/', views.create_new_user_view, name='signup')
]

urlpatterns += staticfiles_urlpatterns()