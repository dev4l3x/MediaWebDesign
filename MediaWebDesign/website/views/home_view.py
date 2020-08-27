from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service, SocialNetwork, Video, Image


def index(request):
    template = loader.get_template('home.html')
    services = Service.objects.all()
    social_networks = SocialNetwork.objects.all()
    videos = Video.objects.all()
    photos = Image.objects.all()
    context = {
        'photos': photos,
        'videos': videos,
        'services': services,
        'networks': social_networks
    }
    return HttpResponse(template.render(context, request))
