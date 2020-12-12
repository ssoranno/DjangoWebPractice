from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.http import HttpResponse
from django.shortcuts import render
from storage.models import Meeting
from storage.models import Contact
from storage.models import CyberSkill
from storage.models import DevSkill
from storage.models import CloudPlatform
from django.core.mail import send_mail

# Create your views here.
def welcome(request):
    return render(request, "mainapp/welcome.html", {"meetings": Meeting.objects.all(), "CyberSkills": CyberSkill.objects.all()})#, {"CyberSkills" : CyberSkill.objects.all()})

def contactPage(request, id):
    contact = get_object_or_404(Contact, pk=id)
    return render(request, "mainapp/contact.html", {"Contact": contact})

def meetingPage(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "mainapp/meeting.html", {"Meeting": meeting})

ContactForm = modelform_factory(Contact, exclude=[])


def newContact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        #if form.is_valid():
        form.save()
        return redirect("welcome")
        # form has been submitted, process data
    else:
        form = ContactForm()
        return render(request, "mainapp/ContactMe.html", {"form": form})