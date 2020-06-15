# Create your views here.
# coding=utf-8

from PIL import Image
from django.core.paginator import Paginator, InvalidPage, EmptyPage, \
    PageNotAnInteger
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, render_to_response, \
    HttpResponse
from forms import ContactForm, PictureForm
from models import Doc, Topic, Admin, Member, Site
import ImageFile
import datetime
#import StringIO
from django.core.mail import send_mail


def login(request):
    if request.method == 'GET':
        
        login = Admin.objects.all()
        return render_to_response('admin/login.html', {'login':login})

    if request.method == 'POST':
        admin_name = request.POST.get('admin_name')
        admin_password = request.POST.get('admin_password')
        admin_error = '用户名或密码错误！'
        
        user = Admin.objects.filter(admin_name=admin_name,admin_password=admin_password)
        
        if user:
            request.session['admin_name']=user
            return HttpResponseRedirect('index.html') 
        else: 
            return render_to_response('admin/error.html',{'admin_error':admin_error})

def admintitle(request):
    return render_to_response('/admin/admintitle.html')    
    
def admin_top(request):
    return render_to_response('admin/admin_top.html')

def out(request):
    
    request.session['username']=''
    outsuccess= '退出成功！'
    return render_to_response('admin/out.html', {'outsuccess': outsuccess})  

def index(request):
    
    if request.method == 'GET':
        
        return render_to_response('admin/index.html')

def list(request):
    
    if request.method == 'GET':
        return render_to_response('admin/left.html')

def edit(request):
    if request.method == 'GET':

        return render_to_response('admin/right.html')

def siteconfig(request):
    
    if request.method == 'GET':
        return render_to_response('admin/siteconfig.html')
    
    if request.method == 'POST':
        
        sitename = request.POST.get('sitename')
        keywords = request.POST.get('keywords')
        descriptions = request.POST.get('descriptions')
        copyrightinfo = request.POST.get('copyrightinfo')
        
        
        form = PictureForm(request.POST, request.FILES)  
        if form.is_valid(): 
            if 'login' and 'banner' in request.FILES:
                login = request.FILES["login"]  
                banner = request.FILES["banner"]
            else:
                login = None
                banner = None
            parser = ImageFile.Parser()  
            for chunk in login.chunks() and banner.chunks():  
                parser.feed(chunk)  
        
                site = Site()
                site.sitename = sitename
                site.keywords = keywords
                site.descriptions = descriptions
                site.login = login
                site.banner = banner
                site.copyrightinfo = copyrightinfo
                
                site.save()
        return render_to_response('admin/siteconfig.html')

def adsettings(request):
    return render_to_response('admin/adsettings.html')

#-------------------------------栏目操作管理--------------------------------------

def topiclist(request):
    
    topic = Topic.objects.all()
        
    after_range_num = 5       
    befor_range_num = 4       
    try:                   
        page = int(request.GET.get("page", 1))
        if page < 1:
             page = 1
    except ValueError:
            page = 1
    paginator = Paginator(topic, 10)   
    try:                     
        topic_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        topic_list = paginator.page(paginator.num_pages)
        conter = paginator.num_pages
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]

    return render_to_response('admin/topiclist.html',{'topic':topic_list, 'page_range':page_range})

def addtopic(request):
    
    if request.method == 'GET':

        topic = Topic.objects.all()
        return render_to_response('admin/addtopic.html', {'topic':topic})

    if request.method == 'POST':
        
        bigtopic = request.POST.get('bigtopic')
        success = '操作成功！' 
        failure='发布不成功，请确认信息填充完整后重新发布！'
       
        topic = Topic()
        topic.bigtopic = bigtopic
        
        if topic.bigtopic == '':
            return render_to_response('admin/failure.html',{'failure': failure})
        
        else:
            topic.save()
            return render_to_response('admin/success.html', {'success':success})

def modifytopic(request, id):
    
    
    if request.method == 'GET':
        topic = Topic.objects.get(id=id)
        return render_to_response('admin/modifytopic.html', {'topic':topic})
    
    if request.method == 'POST':
        
        topic = Topic.objects.get(id=id)
        
        bigtopic = request.POST.get('bigtopic')
        success = '操作成功！'
    
        topic.bigtopic = bigtopic
        
        if topic.bigtopic == '':
            return render_to_response('admin/failure.html',{'failure': failure})
        
        else:
            topic.save()
            return render_to_response('admin/success.html', {'success':success})
        
def deltopic(request, id):
    
    topic = Topic.objects.get(id=id)
    topic.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

#-------------------------------栏目内容管理--------------------------------------
def askanswer(request):
    return render_to_response('admin/askanswer.html')
def information(request):
    
    info = Doc.objects.all()
    #sorts = Sort.objects.all()[0:3]
   # now = datetime.datetime.now().__format__("%Y-%m-%d")
        
    after_range_num = 5       
    befor_range_num = 4       
    try:                   
        page = int(request.GET.get("page", 1))
        if page < 1:
             page = 1
    except ValueError:
            page = 1
    paginator = Paginator(info, 10)   
    try:                     
        info_list = paginator.page(page)
    except(EmptyPage, InvalidPage, PageNotAnInteger):
        info_list = paginator.page(paginator.num_pages)
        conter = paginator.num_pages
    if page >= after_range_num:
        page_range = paginator.page_range[page - after_range_num:page + befor_range_num]
    else:
        page_range = paginator.page_range[0:int(page) + befor_range_num]

    return render_to_response('admin/information.html',{'info':info_list, 'page_range':page_range})

def addinfo(request):
    
    if request.method == 'GET':

        list = Doc.objects.all()
        return render_to_response('admin/addinfo.html', {'lists':list})

    if request.method == 'POST':
        
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        source = request.POST.get('source')
        author = request.POST.get('author')
        time = request.POST.get('calendar')
        content = request.POST.get('content')
        success = '成功发布！' 
        failure='发布不成功，请确认信息填充完整后重新发布！'
       
        doc = Doc()
        doc.title = title
        doc.source = source
        doc.time = time
        doc.author = author
        doc.content = content
        
        if doc.summary == '':
            doc.summary = doc.content[0:30]
        else:
            doc.summary = summary
        
        if doc.title == '' or doc.source == '' or doc.author == '' or doc.title == '' or doc.content == '':
            return render_to_response('admin/failure.html',{'failure': failure})
        
        else:
            doc.save()
            return render_to_response('admin/success.html', {'success':success})

def modifyinfo(request, id):
    
    if request.method == 'GET':
        info = Doc.objects.get(id=id)
        return render_to_response('admin/modifyinfo.html', {'info':info})
    
    if request.method == 'POST':
        
        doc = Doc.objects.get(id=id)
        
        title = request.POST.get('title')
        source = request.POST.get('source')
        author = request.POST.get('author')
        time = request.POST.get('calendar')
        content = request.POST.get('content')
    
        doc.title = title
        doc.source = source
        doc.author = author
        doc.time = time
        doc.content = content
        doc.save()
        
        return HttpResponseRedirect('/admin/information.html')
            
def delinfo(request, id):
    info = Doc.objects.get(id=id)
    info.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def digest(request):
    return render_to_response('admin/digest.html')
def announcement(request):
    return render_to_response('admin/announcement.html')
def about(request):
    return render_to_response('admin/about.html')

#------------------------------注册用户管理------------------------------------
def member(request):
    return render_to_response('admin/member.html')
def leaveamsg(request):
    return render_to_response('admin/leaveamsg.html')
def reply( request):
    return render_to_response('admin/reply.html')
def comment(request):
    return render_to_response('admin/comment.html')

#-------------------------------Index-----------------------------------------
    
def ilogin(request):
    
    return render_to_response('login.html')   


def register(request):
     
    return render_to_response('register.html')   
    
def getIndex(request):    
    
    doc = Doc.objects.order_by('-id').all()[0:8]
    now = datetime.datetime.now().__format__('%Y-%m-%d %X')

    return render_to_response('index.html', {'doc':doc, 'now': now})

#import time
def getInfo(request, id):

    info = Doc.objects.get(id=id)
    info.hits += 1
    info.save()
#    now = datetime.datetime.now().__format__('%Y-%m-%d %X')
#    now = time.strftime('%Y-%m-%d %X',time.localtime())
   
#    list=[]
#    for s in doc:
#        m=s.content[0:8]
#        list.append(m)
#        q=list[0]
    client_ip = request.META['REMOTE_ADDR']
    return render_to_response('info.html', { 'info':info, 'ip':client_ip})


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
                Q(sid__icontains=query) | 
                Q(title__icontains=query) | 
                Q(author__icontains=query)
                )
        results = Topic.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("search.html", {"results": results, "query": query})

def contact(request): 
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid(): 
            topic = form.cleaned_data['topic'] 
            message = form.cleaned_data['message'] 
            sender = form.cleaned_data.get('sender', 'noreply@example.com') 
            send_mail(
                      'Feedback from your site, topic: %s' % topic,
                      message, sender,
                      ['administrator@example.com'] 
            ) 
            return HttpResponseRedirect('/contact/')
    else: 
        form = ContactForm() 

    return render_to_response('contact.html', {'form': form})

    

