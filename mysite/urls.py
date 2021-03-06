from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin

from mysite.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^home/changestatus/$',core_views.change_status),
    url(r'^home/add/$',core_views.addcomp),
]
