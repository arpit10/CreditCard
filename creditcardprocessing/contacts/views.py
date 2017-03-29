from django.core.mail import send_mail
from django.shortcuts import render
from forms import ContactForm
from django.conf import settings


def contact(request):
    title = 'Contact'
    form = ContactForm(request.POST or None)
    confirm_message = None

    if form.is_valid():
        print form.cleaned_data['email']
        subject = "Message from MySite"
        message = '%s %s' %(form.cleaned_data['comment'], form.cleaned_data['name'])
        emailFrom = form.cleaned_data['email']
        emailTo=[settings.EMAIL_HOST_USER]
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False)
        title = "Thanks!"
        confirm_message = "Thanks for the message. We will get right back to you"

    context = {'title': title, 'form': form, 'confirm_message': confirm_message}
    template = "contact.html"
    return render(request, template, context)