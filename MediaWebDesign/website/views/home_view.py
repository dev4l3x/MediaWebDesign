from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service


def index(request):
    template = loader.get_template('index.html')
    services = Service.objects.all()
    context = {
        'services': services
    }
    return HttpResponse(template.render(context, request))
