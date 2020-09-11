from django.urls import path
from PersonalSite_Application.Views import homeView

urlpatterns = [
    path('', homeView.index),
    path('modalRendering/<id>', homeView.workSampleInfoModal),
    path('saveMessage', homeView.saveMessage, name='sendMsg'),
]
