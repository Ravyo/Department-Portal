from django.urls import path
from .import views


app_name = 'students'
urlpatterns = [
    path('', views.index, name='studentshome'),
    path('<int:student_id>/studentdetail/',views.student_detail,name='student_detail')
]
