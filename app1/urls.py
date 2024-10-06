from django.urls import path
from app1 import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('1/',views.index1,name = 'login'),
    path('2/',views.index2,name ='signup'),
    path('3/',views.index3,name ='calender'),
    path('4/',views.index4,name ='sett'),
    path('5/',views.index5,name ='symptoms'),
    path('6/',views.index6,name ='diet'),       
    path('7/',views.index7,name ='shop'), 
   # path('8/',views.index8,name ='remainders'),
   # path('8/', views.index8, name='signup'), 
    #path('9/', views.index9, name='setting'),
    #path('10/', views.index10, name='add_to_cart'),
]