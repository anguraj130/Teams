from django.forms import ModelForm
from.models import Certifications

class CertificateForm(ModelForm):
     class Meta:
        model = Certifications
        fields = '__all__'