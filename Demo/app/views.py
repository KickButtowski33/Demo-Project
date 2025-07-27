from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    html = render_to_string('home.html')
    return HttpResponse(html)

def about(request):
    html = render_to_string('about.html')
    return HttpResponse(html)

def contact(request):
    html = render_to_string('contact.html')
    return HttpResponse(html)

def services(request):
    html = render_to_string('services.html')
    return HttpResponse(html)

def portfolio(request):
    html = render_to_string('portfolio.html')
    return HttpResponse(html)

def blog(request):
    html = render_to_string('blog.html')
    return HttpResponse(html)

def testimonials(request):
    html = render_to_string('testimonials.html')
    return HttpResponse(html)

def faq(request):
    html = render_to_string('faq.html')
    return HttpResponse(html)

def pricing(request):
    html = render_to_string('pricing.html')
    return HttpResponse(html)