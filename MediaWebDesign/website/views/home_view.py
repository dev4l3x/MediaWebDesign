from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service, SocialNetwork, Video, Image, PortfolioImage, Brand
from dynamic_preferences.registries import global_preferences_registry
from django.core.files.uploadedfile import SimpleUploadedFile



def index(request):


    # We instantiate a manager for our global preferences
    global_preferences = global_preferences_registry.manager()

    template = loader.get_template('home.html')
    social_networks = SocialNetwork.objects.all()
    services = Service.objects.all()
    videos = Video.objects.all()
    photos = PortfolioImage.objects.all()
    brands = Brand.objects.all()
    logo = global_preferences['general__Background']
    context = {
        'logo': logo,
        'photos': photos,
        'videos': videos,
        'networks': social_networks,
        'services': services,
        'brands': brands,
        'active': 0
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
