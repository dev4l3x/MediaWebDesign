from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service, SocialNetwork, Video, Image, PortfolioImage


def index(request):
    template = loader.get_template('home.html')
    social_networks = SocialNetwork.objects.all()
    videos = Video.objects.all()
    photos = PortfolioImage.objects.all()
    context = {
        'photos': photos,
        'videos': videos,
        'networks': social_networks,
        'active': 0
    }
    return HttpResponse(template.render(context, request))


def about(request):
    template = loader.get_template('about.html')
    services = Service.objects.all()
    social_networks = SocialNetwork.objects.all()

    context = {
        'networks': social_networks,
        'services': services,
        'active': 2
    }

    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        email = request.POST.get('email')


def gallery(request):
    template = loader.get_template('gallery.html')

    images = Image.objects.all()
    context = {
        'images': images
    }

    return HttpResponse(template.render(context, request))
