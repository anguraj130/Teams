from django.shortcuts import render
from .Forms import CertificateForm
from.models import Info,Du_lead,Manager,Ams,Leads,Certifications

# Create your views here.
def index(request):
    information = Info.objects.all()
    du_lead = Du_lead.objects.all()
    manager = Manager.objects.all()
    ams = Ams.objects.all()
    leads = Leads.objects.all()
    return render(request, 'index.html', {'information': information, 'du_lead': du_lead, 
    'manager': manager, 'ams': ams, 'leads': leads})

def leave(request):
    return render(request, 'leave.html')

def projects(request):
    return render(request, 'project.html')

def certifications(request):

    form = CertificateForm()
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'certification.html', context)

def team(request):
    return render(request, 'team.html')