from dynamic_preferences.types import BooleanPreference, StringPreference, LongStringPreference, FilePreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from django.conf import settings
from dynamic_preferences.users.registries import user_preferences_registry
import os
import shutil


general = Section('general')

@global_preferences_registry.register
class WebDescription(LongStringPreference):
    section = general
    name = 'Description'
    verbose_name = 'Description'
    default = ''
    required = True


@global_preferences_registry.register
class WebBackground(FilePreference):
    section = general
    name = 'Background'
    verbose_name = 'Background'

    def validate(self, value):
        folder = os.path.join(settings.MEDIA_ROOT, 'dynamic_preferences', 'general__Background')
        if not os.path.isdir(folder):
            return
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


@global_preferences_registry.register
class WebLogo(FilePreference):
    section = general
    name = 'Logo'
    verbose_name = 'Logo'

    def validate(self, value):
        folder = os.path.join(settings.MEDIA_ROOT, 'dynamic_preferences', 'general__Logo')
        if not os.path.isdir(folder):
            return
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


@global_preferences_registry.register
class GalleryLogo(FilePreference):
    section = general
    name = 'GalleryLogo'
    verbose_name = 'Gallery logo'

    def validate(self, value):
        folder = os.path.join(settings.MEDIA_ROOT, 'dynamic_preferences', 'general__GalleryLogo')
        if not os.path.isdir(folder):
            return
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))


@global_preferences_registry.register
class ShareImage(FilePreference):
    section = general
    name = 'ShareImage'
    verbose_name = 'Share logo'

    def validate(self, value):
        folder = os.path.join(settings.MEDIA_ROOT, 'dynamic_preferences', 'general__ShareImage')
        if not os.path.isdir(folder):
            return
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
