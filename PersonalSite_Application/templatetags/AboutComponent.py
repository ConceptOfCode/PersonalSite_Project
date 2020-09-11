from PersonalSite_Application.models.PersonalSiteModel import *
from django import template

register = template.Library()


@register.inclusion_tag('views/aboutViewComponent.html')
def rendering():
    profileData = Profile.objects.values('id', 'firstName', 'lastName', 'Email', 'phoneNumber', 'birthDate').get(
        Status=1)

    aboutData = AboutMe.objects.select_related('Profile').filter(
        Profile__Status=1).values('aboutTitle', 'aboutFullText')[0]

    skillsData = Skills.objects.select_related('Profile').filter(Profile__Status=1).values('skillName', 'skillValue')

    # متن های داخل دیتابیس رو به سه تا پاراگراف تبدیل کردم
    aboutData['aboutFullText'] = aboutData['aboutFullText'].split('$$')

    context = {
        'data': {
            'profileInfo': profileData,
            'skillsInfo': skillsData,
            'aboutInfo': aboutData
        },
        'status': 200
    }
    return context
