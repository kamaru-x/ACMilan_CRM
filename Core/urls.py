from Core import views
from django.urls import path

urlpatterns = [
    path('add_center/',views.add_center,name='add_center'),
    path('list_leads/',views.list_center,name='list_center'),
    path('add-coordinator/',views.add_coordinator,name='add_cordinator'),
    path('list-coordinators/',views.list_coordinators,name='list_cordinator'),
    path('add-lead/',views.add_lead,name='add_lead'),
    path('list-leads/',views.list_leads,name='list_leads'),
    path('view_lead/<int:id>/',views.view_lead,name='view_lead'),
    path('add-student/',views.add_student,name='add_student'),
    path('list-students/',views.list_students,name='list_students'),
]