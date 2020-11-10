from django.shortcuts import render
from.models import Info,Du_lead,Manager,Ams,Leads

# Create your views here.
def index(request):
    information = Info.objects.all()
    du_lead = Du_lead.objects.all()
    manager = Manager.objects.all()
    ams = Ams.objects.all()
    leads = Leads.objects.all()
    return render(request, 'index.html', {'information': information, 'du_lead': du_lead, 
    'manager': manager, 'ams': ams, 'leads': leads})

