from django.contrib import admin

# Register your models here.
from models import SiteUser, UserCategory,Activity, VisitorLog
# Register your models here.

admin.site.register(Activity)
admin.site.register(SiteUser)
admin.site.register(VisitorLog)
admin.site.register(UserCategory)
