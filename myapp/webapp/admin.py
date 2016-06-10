from django.contrib import admin

# Register your models here.
from models import User, UserCategory,Activity 
# Register your models here.

admin.site.register(Activity)
admin.site.register(User)
admin.site.register(UserCategory)
