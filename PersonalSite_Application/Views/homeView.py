from django.shortcuts import render
from PersonalSite_Application.models.PersonalSiteModel import * 
from django.http import JsonResponse
from persiantools.jdatetime import JalaliDate
from django.core.mail import send_mail
import ghasedak


def index(request):
    context = {
        'title': 'صفحه شخصی || حمید سالارمرادی'
    }
    return render(request, 'views/indexView.html', context)


def workSampleInfoModal(request, id):
    data = WorkSamples.objects.all().select_related('Profile').values('workSampleTitle',
                                                                      'workSampleFullDescriptions',
                                                                      'WorkSampleDoDate',
                                                                      'employerSpecifications',
                                                                      'gitLink').get(pk=id, Status=1)
    context = {}
    if data is not None:
        context['data'] = data
        context['status'] = 200
    else:
        context['status'] = 404

    return render(request, 'views/modalView.html', context)


def saveMessage(request):
    context = {}

    try:
        assert request.method == 'POST'
    except:
        context['status'] = 501
        context['statusText'] = 'یک خطا در سمت سرور رخ داده است. دوباره تلاش کنید'

        return JsonResponse(context)

    try:
        postData = request.POST
        message = MessagesReceived()
        message.FullnameSender = postData['name']
        message.emailSender = postData['email']
        message.phoneNumberSender = postData['phone']

        if len(message.phoneNumberSender) > 11:
            realPhone = []
            for i in range(0, 11):
                realPhone.append(postData['phone'][i])
            message.phoneNumberSender = ''
            message.phoneNumberSender = ''.join(realPhone)

        message.messageText = postData['message']
        message.createDateTime = JalaliDate.today()
        message.Profile_id = Profile.objects.all().values(
            'id').get(Status=1)['id']
        message.save()

        sendEmail(postData['message'], postData['name'])
        # sendSMS()

        context['status'] = 200
        context['statusText'] = 'پیام شما با موفقیت برای من ارسال شد.'
        context['infoText'] = 'اگر پیام شما درخواست همکاری بوده به زودی با شما ارتباط میگیرم'

        return JsonResponse(context)
    except Exception as e:
        context['status'] = 501
        context['statusText'] = 'یک خطا در سمت سرور رخ داده است. اطلاعات خود را دوباره بررسی کنید!'
        return JsonResponse(context)


def sendSMS():
    sms = ghasedak.Ghasedak(
        "4f6ea7feb088eddeef32735843ca31864b6d44c4fcb0a9911a0d6cb952c45e69")
    sms.send({'message': "حمید داخل سایت برا پیام گذاشتن",
              'receptor': "09154860551", 'linenumber': "10008566"})


def sendEmail(body, nameSender):
    send_mail(
        nameSender + ' ' + 'یک پیام برای شما ارسال کرد',
        body + '\n' + 'تاریخ ارسال : ' + JalaliDate.today(),
        'salarmoradi.h@gmail.com',
        ['salarmoradi.h@gmail.com'],
        fail_silently=False,
    )
