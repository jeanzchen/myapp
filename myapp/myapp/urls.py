from django.conf.urls import include, url
from django.contrib import admin

from webapp import views
from webapp.models import  UserCategory, User

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
UserCategory_detail  = DetailView.as_view(model=UserCategory)
UserCategory_list  = ListView.as_view(model=UserCategory)

User_list  = ListView.as_view(model=User)

urlpatterns = [
    # Examples:
    # url(r'^$', 'myapp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^admin/$', views.admin), 
    url(r'^userCategory/$', UserCategory_list, name="UserCategory_list" ),
    #url(r'^userCategory/$', views.UserCategoryListView.as_view(), name="UserCategory_list" ),
    url(r'^userCategory/add/$', views.UserCategoryCreateView.as_view(), name="UserCategoryCreateView" ),
    url(r'^userCategory/(?P<pk>\d+)/$', views.UserCategoryUpdateView.as_view(), name="UserCategoryUpdateView" )
    ,

    url(r'^user/$', User_list, name="User_list" ),
    url(r'^user/add/$', views.UserCreateView.as_view(), name="userCreateView" ),
    url(r'^user/(?P<pk>\d+)/$', views.UserUpdateView.as_view(), name="userUpdateView" )
    ]
