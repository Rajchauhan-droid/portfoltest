from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.mail import BadHeaderError, EmailMessage
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

from socket import timeout

def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            content = form.cleaned_data['content']
            try:
                email = EmailMessage(
                    contact_name,
                    content,
                    contact_email,
                    ['raajchauh@gmail.com'],  # Change to your email
                    reply_to=[contact_email],
                )
                email.send()
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            except timeout:
                return HttpResponse('Email server took too long to respond. Please try again later.')
            return redirect('main:contact')
    return render(request, 'ports/contact.html', {'form': form})

def base(request):
    return render(request, 'ports/base.html')


def home(request):
    return render(request, 'ports/home.html')

def about(request):
    return render(request, 'ports/about.html')

def services(request):
    return render(request, 'ports/services.html')

def portfolio(request):
    return render(request, 'ports/portfolio.html')


