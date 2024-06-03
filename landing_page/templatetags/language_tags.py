from django import template
from django.utils.translation import get_language
from django.conf import settings

register = template.Library()

@register.simple_tag
def get_current_language_display():
    current_language = get_language()
    return dict(settings.LANGUAGES).get(current_language)

@register.filter
def custom_redir_lang(url_fullpath, lang):
    """
    This filter removes the current language prefix and adds the new language prefix.
    """
    ls_urls = url_fullpath.split('/')
    if len(ls_urls) > 1 and ls_urls[1] in dict(settings.LANGUAGES).keys():
        del ls_urls[1]
    return f"/{lang}/" + '/'.join(ls_urls[1:])