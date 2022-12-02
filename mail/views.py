from django.http import HttpResponse
from mail.models import Resident
from django.template import loader
def index(request):
    resident_list = Resident.objects.order_by('-name')[:5]
    template = loader.get_template('mail/index.html')
    context = {
        'resident_list': resident_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, resident_id):
    # resident = Resident.objects.get(pk=resident_id)
    resident_list = Resident.objects.order_by('-name')[:5]
    output = ', '.join([r.name for r in resident_list])
    # return HttpResponse("You're looking at resident id %s and their name is %s." % (resident.pk, resident.name))
    return HttpResponse(output)


from django.shortcuts import render

# Create your views here.
