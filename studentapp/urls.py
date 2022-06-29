from . import views
from django.urls import path

urlpatterns = [
    path('add_student1',views.add_student1,name='add_student1'),
    path('add_student_details',views.add_student_details,name='add_student_details'),
    path('show_student',views.show_student,name='show_student'),
    path('ind_details/<int:pk>',views.ind_details,name='ind_details'),
   
    path('edit/<int:pk>',views.edit,name='edit'),
    path('edit_student/<int:pk>',views.edit_student,name='edit_student'),
    path('delete/<int:pk>',views.delete,name='delete'),
  
 
]