from django import template
from PersonalSite_Application.models.PersonalSiteModel import *

register = template.Library()


@register.inclusion_tag('views/ServicesViewComponent.html')
def rendering():
    data = Services.objects.all().filter(Status=1).order_by('serviceOrder')
    context = {
        'data': data,
        'Status': 200
    }
    return context
