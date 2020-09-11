from django.core.validators import MaxLengthValidator
from django.db import models


class Profile(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    birthDate = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    phoneNumber = models.IntegerField(validators=[MaxLengthValidator(12)])
    Photo = models.CharField(max_length=100)
    whatsAppLink = models.CharField(max_length=100)
    telegramLink = models.CharField(max_length=50)
    instagramLink = models.CharField(max_length=50)
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.PositiveIntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)


class AboutMe(models.Model):
    aboutTitle = models.CharField(max_length=50)
    aboutFullText = models.CharField(max_length=2000)
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.PositiveIntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Skills(models.Model):
    skillName = models.CharField(max_length=50)
    skillValue = models.PositiveIntegerField(validators=[MaxLengthValidator(3)])
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.PositiveIntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Services(models.Model):
    serviceTitle = models.CharField(max_length=50)
    serviceDescriptions = models.CharField(max_length=200)
    serviceOrder = models.PositiveIntegerField(validators=[MaxLengthValidator(3)])
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.IntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class WorkSamples(models.Model):
    workSampleTitle = models.CharField(max_length=50)
    workSampleFullDescriptions = models.CharField(max_length=300)
    WorkSampleDoDate = models.CharField(max_length=20)
    employerSpecifications = models.CharField(max_length=50)
    gitLink = models.CharField(max_length=100)
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.IntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class MessagesReceived(models.Model):
    FullnameSender = models.CharField(max_length=150)
    emailSender = models.CharField(max_length=150)
    phoneNumberSender = models.CharField(max_length=13)
    messageText = models.CharField(max_length=800)
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)


class Universities(models.Model):
    uniName = models.CharField(max_length=50)
    uniDescriptions = models.CharField(max_length=100)
    # uniImage = models.ImageField(null=True)
    uniEnterDate = models.CharField(max_length=12, null=True)
    uniYearsEducation = models.PositiveIntegerField(MaxLengthValidator(2))
    uniDegree = models.CharField(max_length=50, null=True)
    uniMajor = models.CharField(max_length=50, null=True)
    uniCity = models.CharField(max_length=50, null=True)
    createDateTime = models.CharField(max_length=20, blank=True, null=True)
    Status = models.IntegerField(validators=[MaxLengthValidator(1)], blank=True, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
