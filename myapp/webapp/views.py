from django.shortcuts import render, render_to_response, HttpResponse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from datetime import datetime
from webapp.models import  VisitorLog, SiteUser, UserCategory, Activity
import xlwt
# Create your views here.

def index(request):
    return render_to_response("index.html")

def admin(request):
    return render_to_response("admin.html")

def contactUs(request):
    return render_to_response("webapp/contact-us.html")

def aboutUs(request):
    return render_to_response("webapp/about-us.html")

def generate_excel(request):
        #books = Book.objects.all()
        visitorLogs = VisitorLog.objects.all().values_list('LogId', 'category', 'fname', 'lname', 'phone', 'email', 'UserToVisit', 'dept', 'comment', 'nowtime')
        print 'gymvisitorLogs=', visitorLogs
        # Create the HttpResponse object with Excel header.This tells browsers that 
        # the document is a Excel file.
        response = HttpResponse(content_type='application/ms-excel')

        # The response also has additional Content-Disposition header, which contains 
        # the name of the Excel file.
        response['Content-Disposition'] = 'attachment; filename=gymvisitos.xls'

        # Create object for the Workbook which is under xlwt library.
        workbook = xlwt.Workbook()

        # By using Workbook object, add the sheet with the name of your choice.
        worksheet = workbook.add_sheet("visitors")
        
        row_num = 0
        columns =['LogId', 'category', 'fname', 'lname', 'phone', 'email', 'UserToVisit', 'dept', 'comment', 'nowtime']
        for col_num in range(len(columns)):
            # For each cell in your Excel Sheet, call write function by passing row number, 
            # column number and cell data.
            worksheet.write(row_num, col_num, columns[col_num])     
       
        for row in visitorLogs:
            row_num += 1
            #print "log=", log
            #row = [log.Type, log.fname, log.lname, log.email, log.phone, log.Comments, log.CreatedOn]
            print 'row=', row
            for col_num in range(len(row)):
                print 'row[%d]=%s'%(col_num, str(row[col_num]))
                worksheet.write(row_num, col_num, str(row[col_num]))
       
        workbook.save(response)
        return response

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
    model = SiteUser
    template_name = "webapp/siteuser_list.html"
    paginate_by = 10
    print 'UserList'
'''
     
class UserCreateView(CreateView):
    model = SiteUser
    template_name = "webapp/siteuser_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'empid', 'phone', 'email', 'dept', 'comment', 'nowtime']
    success_url = '/user/'
    print 'User create'

class UserUpdateView(UpdateView):
    model =SiteUser
    template_name = "webapp/siteuser_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'empid', 'phone', 'email', 'dept', 'comment', 'nowtime']
    print 'User update'
    success_url = '/user/'
    
class ActivityCreateView(CreateView):
    model = SiteUser
    template_name = "webapp/activity_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    success_url = '/activity/'
    print 'Activity create'

class ActivityUpdateView(UpdateView):
    model = SiteUser
    template_name = "webapp/activity_detail.html"
    fields =['UserId', 'category', 'fname', 'lname', 'acttype']
    print 'Activity update'
    success_url = '/activity/'  
    
###
class VisitorLogCreateView(CreateView):
    model = VisitorLog
    template_name = "webapp/visitorLog_detail.html"
    fields =['LogId', 'category', 'fname', 'lname', 'phone', 'email', 'UserToVisit', 'dept', 'comment', 'nowtime']
    success_url = '/visitorLog/add/'
    print 'Visitor log create'