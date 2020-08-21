from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service, SocialNetwork


def index(request):
    template = loader.get_template('about.html')
    services = Service.objects.all()
    social_networks = SocialNetwork.objects.all()
    context = {
        'services': services,
        'networks': social_networks
    }
    return HttpResponse(template.render(context, request))
