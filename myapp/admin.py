from django.contrib import admin
from .models import Group,User,Chat,Message


admin.site.register(User)
admin.site.register(Group)
admin.site.register(Chat)
admin.site.register(Message)