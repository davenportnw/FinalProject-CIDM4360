from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailRecipients, EmailMessage
from django.http import HttpResponse
from mail.models import Resident, Package
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from mail.forms import PackageForm


@login_required(login_url='/accounts/login/')
def index(request):
    resident_list = Resident.objects.order_by('-name')[:5]
    template = loader.get_template('mail/index.html')
    context = {
        'resident_list': resident_list,
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def residents(request):
    # resident = Resident.objects.get(pk=resident_id)
    resident_list = Resident.objects.order_by('-name').all()
    template = loader.get_template('mail/residents.html')
    context = {
        'resident_list': resident_list,
    }
    # return HttpResponse("You're looking at resident id %s and their name is %s." % (resident.pk, resident.name))
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def history(request, resident_id):
    person = Resident.objects.get(pk=resident_id)
    packages = Package.objects.filter(owner=person)
    template = loader.get_template('mail/history.html')
    context = {
        'resident': person,
        'packages': packages
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
def package_form_view(request):
    template = loader.get_template('mail/package-form.html')
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            # send email for pending packages
            # check if owner is a resident to send confirmation email (owner is not null)
            person = Resident.objects.get(unit_number=form.cleaned_data['address'], name=form.cleaned_data['name'])
            # Create the EmailClient object that you use to send Email messages.
            email_client = EmailClient.from_connection_string(
                "endpoint=https://davenportcommunicationservices.communication.azure.com/;accesskey=rsWSCkRLpfKj8EdyFnQCg/zGb/sNM9P2sf1g66vMQvgN5gkmQEnUx8M4VtdFrw8CmudfLJ3yB5bP7xOLjchP/A==")
            content = EmailContent(
                subject="Package Notification",
                plain_text="Hello, We have received a package in the office for you. Due to limited storing space, "
                           "you will have 5 days to pick up your package. Or it will be sent back with the post "
                           "office. Thank you!",
            )
            address = EmailAddress(email=person.email)
            recipients = EmailRecipients(to=[address])
            message = EmailMessage(
                sender="DoNotReply@28e4fcda-9e29-469d-bb7a-c27455b91f5f.azurecomm.net",
                content=content,
                recipients=recipients
            )
            email_response = email_client.send(message)
            response = redirect('/mail/packages')
            return response
    else:
        form = PackageForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))


@login_required(login_url='/accounts/login/')
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


@login_required(login_url='/accounts/login/')
def pickup(request):
    package_id = request.POST.get('package_id')
    package = Package.objects.get(pk=package_id)
    package.status = 'DELIVERED'
    package.save()
    response = redirect('/mail/packages')
    return response


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...


def logout_view(request):
    logout(request)
