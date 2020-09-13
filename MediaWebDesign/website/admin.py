from django.contrib import admin
from .models import Language, Video, Image, Service, SocialNetwork, ServiceTranslate, VideoTranslate, PortfolioImage


class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'source')
    readonly_fields = ('thumbnail_preview',)

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Preview'
    thumbnail_preview.allow_tags = True


# Register your models here.
admin.site.register(Language)
admin.site.register(Video)
admin.site.register(Image, ImageAdmin)
admin.site.register(SocialNetwork)
admin.site.register(Service)
admin.site.register(ServiceTranslate)
admin.site.register(VideoTranslate)
admin.site.register(PortfolioImage, ImageAdmin)
