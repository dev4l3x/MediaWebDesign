from django.http import HttpResponse
from django.views import View
from django.template import loader
from website.models import Service, SocialNetwork, Video, Image, PortfolioImage, Brand, Message, ContactReason
from dynamic_preferences.registries import global_preferences_registry
from django.core.files.uploadedfile import SimpleUploadedFile
from django.shortcuts import redirect


def index(request):


    # We instantiate a manager for our global preferences
    global_preferences = global_preferences_registry.manager()

    template = loader.get_template('home.html')
    social_networks = SocialNetwork.objects.all()
    services = Service.objects.all()
    videos = Video.objects.all()
    photos = PortfolioImage.objects.all()
    brands = Brand.objects.all()
    contact_reasons = ContactReason.objects.all()
    logo = global_preferences['general__Background']
    context = {
        'logo': logo,
        'photos': photos,
        'videos': videos,
        'networks': social_networks,
        'services': services,
        'brands': brands,
        'contact_reasons': contact_reasons,
        'active': 0
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        reason = request.POST.get('reason')
        message = request.POST.get('message')
        email = request.POST.get('email')

        message = Message(name=name, message=message, email=email, reason=reason)
        message.save()
    return redirect("/")

def gallery(request):
    template = loader.get_template('gallery.html')

    images = Image.objects.all()
    context = {
        'images': images
    }

    return HttpResponse(template.render(context, request))
