from django import template
from PersonalSite_Application.models.PersonalSiteModel import *

register = template.Library()


@register.inclusion_tag('views/universitiesViewComponent.html')
def rendering():
    data = list(
        Universities.objects.all().select_related('profile').filter(Status=1).values('uniName', 'uniDescriptions',
                                                                                     'uniYearsEducation',
                                                                                     'uniDegree'))
    imgCounter = 0
    for i in data:
        imgCounter += 1
        i['imgCounter'] = imgCounter

    context = {
        'data': data,
        'status': 200
    }
    return context
