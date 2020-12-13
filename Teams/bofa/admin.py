from django.contrib import admin
from.models import Info,Manager,Ams,Leads,Du_lead,Certifications

# Register your models here.
admin.site.register(Info),
admin.site.register(Du_lead),
admin.site.register(Manager),
admin.site.register(Ams),
admin.site.register(Leads),
admin.site.register(Certifications),
