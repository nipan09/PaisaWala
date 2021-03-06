from django.conf.urls import url
from django.urls import path
from . import views

#app_name= 'tasks_notes'

urlpatterns= [
      url(r'^login/$', views.login_view, name='login'),
      url(r'^logout/$', views.logout_view, name='logout'),
      url(r'^signup/$',views.signup_view,name="sign up"),
      url(r'add_item', views.additem_view, name='add item'),
      url(r'^budget-info/(?P<username>\w+)/$', views.app_view, name='app'),
      url(r'^budget-info/(?P<username>\w+)/profile/$', views.profile_view, name='profile'),
    ]