from django.conf.urls import url
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


app_name = 'login'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

url(r'^password_change/$',views.password_change,name='password_change'),

url(r'^password_reset/$',views.password_reset,name='password_reset'),
url(r'^password_reset/password_reset_done/$',views.password_reset_done,name='password_reset_done'),


path('password_reset_confirm/<uidb64>/<token>/',views.password_reset_confirm, name='password_reset_confirm'),
url(r'^password_change/$',views.password_change,name='password_change'),
url(r'^password_change_done/$',auth_views.password_change_done,name='password_change_done'),

url(r'^password_reset_complete/$',views.password_reset_complete,name='password_reset_complete'),

]

