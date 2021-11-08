from django.contrib import admin
from nguoidung.models import User, RoomChat
# Register your models here.
# User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'nation', 'dateofbirth', 'email', 'gender')
    search_fields = ('name', 'email',)
    list_filter = ('nation',)

# Room
@admin.register(RoomChat)
class RoomChat(admin.ModelAdmin):
    list_display = ('RoomID',)