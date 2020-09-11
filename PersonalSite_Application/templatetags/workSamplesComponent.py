from django import template
from PersonalSite_Application.models.PersonalSiteModel import *

register = template.Library()


@register.inclusion_tag('views/workSampleViewComponent.html')
def rendering():
    data = list(WorkSamples.objects.all().select_related('Profile').filter(Status=1).values('id', 'workSampleTitle',
                                                                                            'workSampleFullDescriptions',
                                                                                            'WorkSampleDoDate',
                                                                                            'employerSpecifications',
                                                                                            'gitLink'))
    imgCounter = 0
    for i in data:
        imgCounter += 1
        i['imgCounter'] = imgCounter

    context = {
        'data': data,
        'status': 200
    }
    return context
