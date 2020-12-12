from django.urls import path

from . import views

urlpatterns = [
    path('<int:id>', views.meetingPage, name="meetingPage"),
    path('contactme/', views.newContact, name="contactme"),
]