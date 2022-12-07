from django.http import HttpResponse
from mail.models import Resident, Package
from django.template import loader
from django.shortcuts import redirect

from mail.forms import PackageForm


def index(request):
    resident_list = Resident.objects.order_by('-name')[:5]
    template = loader.get_template('mail/index.html')
    context = {
        'resident_list': resident_list,
    }
    return HttpResponse(template.render(context, request))


def residents(request):
    # resident = Resident.objects.get(pk=resident_id)
    resident_list = Resident.objects.order_by('-name').all()
    template = loader.get_template('mail/residents.html')
    context = {
        'resident_list': resident_list,
    }
    # return HttpResponse("You're looking at resident id %s and their name is %s." % (resident.pk, resident.name))
    return HttpResponse(template.render(context, request))


def history(request, resident_id):
    person = Resident.objects.get(pk=resident_id)
    packages = Package.objects.filter(owner=person)
    template = loader.get_template('mail/history.html')
    context = {
        'resident': person,
        'packages': packages
    }
    return HttpResponse(template.render(context, request))


def package_form_view(request):
    template = loader.get_template('mail/package-form.html')
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            response = redirect('/mail/packages')
            return response

    else:
        form = PackageForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


def packages(request):
    template = loader.get_template('mail/packages.html')
    pending_packages = Package.objects.filter(status='PENDING').order_by('-id')
    unknown_packages = Package.objects.filter(status='UNKNOWN').order_by('-id')
    delivered_packages = Package.objects.filter(status='DELIVERED').order_by('-id')
    context = {
        'pending_packages': pending_packages,
        'unknown_packages': unknown_packages,
        'delivered_packages': delivered_packages
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
