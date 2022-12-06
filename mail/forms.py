from django.forms import ModelForm
from mail.models import Package


class PackageForm(ModelForm):
    class Meta:
        model = Package
        fields = ['name', 'address', 'posting_service', 'received', 'status', 'owner']
