from dynamic_preferences.types import BooleanPreference, StringPreference
from dynamic_preferences.preferences import Section
from dynamic_preferences.registries import global_preferences_registry
from dynamic_preferences.users.registries import user_preferences_registry

general = Section('general')


@global_preferences_registry.register
class SiteEmail(StringPreference):
    section = general
    name = 'Email'
    default = ''
    required = True
