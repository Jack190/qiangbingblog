from django.conf.urls.defaults import *
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dtsite/', include('dtsite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)

urlpatterns = patterns('dev.crud.views',
                      (r'^admin/login.html$', 'login'),
                      (r'^admin/out.html$', 'out'),
                      
                      (r'^admin/index.html$', 'index'),
                      (r'^admin/left.html$', 'list'),
                      (r'^admin/right.html$', 'edit'),
                      (r'^admin/admintitle.html$', 'admintitle'),
                      (r'^admin/admin_top.html$', 'admin_top'),
                      
                      (r'^admin/siteconfig.html$', 'siteconfig'),
                      (r'^admin/adsettings.html$', 'adsettings'),
                      
                      (r'^admin/topiclist.html$', 'topiclist'),
                      (r'^admin/addtopic.html$', 'addtopic'),
                      (r'^admin/modify/(.*)$', 'modifytopic'),
                      (r'^admin/delete/(.*)$', 'deltopic'),
                      
                      (r'^admin/askanswer.html$', 'askanswer'),
                      (r'^admin/information.html$', 'information'),
                      (r'^admin/addinfo.html$', 'addinfo'),
                      (r'^admin/modify/(.*)$', 'modifyinfo'),
                      (r'^admin/delete/(.*)$', 'delinfo'),
                      (r'^admin/digest.html$', 'digest'),
                      (r'^admin/announcement.html$', 'announcement'),
                      (r'^admin/about.html$', 'about'),
                      
                      (r'^admin/member.html$', 'member'),
                      (r'^admin/leaveamsg.html$', 'leaveamsg'),
                      (r'^admin/reply.html$', 'reply'),
                      (r'^admin/comment.html$', 'comment'),
                      
#-------------------------index-----------------------------------  
                      (r'^login.html$', 'ilogin'),                    
                      (r'^register.html$', 'register'),                    
                      (r'^index.html$', 'getIndex'),
                      (r'^sort.html$', 'getSort'),
                      (r'^delete/(.*)$', 'delSort'),
                      (r'^info/(.*)$', 'getInfo'),
                      (r'^search/$', 'search'),
                      (r'^contact/$', 'contact')
)
urlpatterns += patterns('',
                       (r'^(?P<path>.+)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)