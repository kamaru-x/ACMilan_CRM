from Core import views
from django.urls import path

urlpatterns = [
    path('add_center/',views.add_center,name='add_center'),
    path('list-centers/',views.list_center,name='list_center'),
    path('view-center/<int:cid>/',views.view_center,name='view_center'),
    path('edit-center/<int:cid>/',views.edit_center,name='edit_center'),

    path('add-coordinator/',views.add_coordinator,name='add_cordinator'),
    path('list-coordinators/',views.list_coordinators,name='list_cordinator'),
    path('edit_coordinator/<int:cid>/',views.edit_coordinator,name='edit_coordinator'),

    path('add-lead/',views.add_lead,name='add_lead'),
    path('list-leads/',views.list_leads,name='list_leads'),
    path('view_lead/<int:id>/',views.view_lead,name='view_lead'),
    path('add-student/',views.add_student,name='add_student'),
    path('view_student/<int:sid>/',views.view_student,name='view_student'),
    path('list-students/',views.list_students,name='list_students'),
    path('accept/<int:lid>/',views.accept,name='accept'),
    path('attandance-centers/',views.center_attandance,name='center_attandance'),
    path('sections/<int:cid>/',views.sections,name='sections'),
    path('attandance/<int:sid>/',views.attandance,name='attandance'),
    path('view-attandance/<int:sid>/',views.view_attandance,name='view_attandance'),
]