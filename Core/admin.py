from django.contrib import admin
from Core.models import Lead,Students,Center,Lead_Updates,Section,Attandance,Coordinator,Lead_Rejection,Payment

# Register your models here.

admin.site.register(Lead)
admin.site.register(Students)
admin.site.register(Center)
admin.site.register(Lead_Updates)
admin.site.register(Section)
admin.site.register(Attandance)
admin.site.register(Coordinator)
admin.site.register(Lead_Rejection)
admin.site.register(Payment)