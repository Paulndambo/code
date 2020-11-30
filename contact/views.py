from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.conf import settings
from . forms import ContactForm
from . models import Message
from . forms import MessageForm
from django.contrib import messages
# Create your views here.
def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None
    
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from David.com'
        message = '%s %s' %(comment, name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        title = 'Thanks'
        send_mail(subject, message, emailFrom, emailTo, fail_silently=True)
        confirm_message = "Thanks for the message, we will get back to you."
        form = None
    context = {
            'title': title,
            'form': form,
            'confirm_message': confirm_message
        }
    
    return render(request, "contact.html", context)

@login_required
def message(request):
    context = {
        "form": MessageForm
    }
    return render(request, 'message.html', context)


def addMessage(request):
    form = MessageForm(request.POST)

    if form.is_valid():
        myregister = Message(name=form.cleaned_data['name'],
                            email=form.cleaned_data['email'],
                            message=form.cleaned_data['message'])

        myregister.save()
        messages.add_message(request, messages.SUCCESS,
                             "Message Send successfully")
    return redirect("home")
