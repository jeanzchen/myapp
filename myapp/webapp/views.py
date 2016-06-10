from django.shortcuts import render, render_to_response
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from models import User, UserCategory, Activity, About, Contact 
# Create your views here.

def index(request):
    return render_to_response("index.html")

def admin(request):
    return render_to_response("admin.html")

class UserCategoryUpdateView(UpdateView):
    model = UserCategory
    template_name = "webapp/usercategory_detail.html"
    fields =['name', 'description']
    success_url = '/userCategory/'
    print 'Update UserCategoryList'
    
class UserCategoryCreateView(CreateView):
    model = UserCategory
    template_name = "webapp/usercategory_detail.html"
    fields =['name', 'description']
    success_url = '/userCategory/'
    print 'Create UserCategoryList'
    
#########################################
'''
class UserListView(ListView):
    model = User
    template_name = "webapp/user_list.html"
    paginate_by = 10
    print 'UserList'
'''
     
class UserCreateView(CreateView):
    model = User
    template_name = "webapp/user_detail.html"
    fields =['UserId', 'category', 'fname', 'lname']
    success_url = '/user/'
    print 'User create'

class UserUpdateView(UpdateView):
    model = User
    template_name = "webapp/user_detail.html"
    fields =['UserId', 'category', 'fname', 'lname']
    print 'User update'
    success_url = '/user/'
    
class ActivityCreateView(CreateView):
    model = User
    template_name = "webapp/activity_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    success_url = '/activity/'
    print 'Activity create'

class ActivityUpdateView(UpdateView):
    model = User
    template_name = "webapp/activity_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    print 'Activity update'
    success_url = '/activity/'  
    
class AboutCreateView(CreateView):
    model = About
    template_name = "webapp/about-us.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    success_url = '/about/'
    print 'About-us provide'  
    
class ContactCreateView(CreateView):
    model = Create
    template_name = "webapp/contact-us.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    success_url = '/contact/'
    print 'Contact-us provide'  
      
      