from django.contrib import admin

# Register your models here.
from member.models import User

admin.site.register(User)