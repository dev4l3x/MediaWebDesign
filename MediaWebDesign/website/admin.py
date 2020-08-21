from django.contrib import admin
from .models import Language, Video, Image, Service, SocialNetwork, ServiceTranslate

# Register your models here.
admin.site.register(Language)
admin.site.register(Video)
admin.site.register(Image)
admin.site.register(SocialNetwork)
admin.site.register(Service)
admin.site.register(ServiceTranslate)
