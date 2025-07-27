from django.http import HttpResponse
import os
import boto3

# Views with simple HTML response
def home(request):
    return HttpResponse("<h1>Welcome to the Home Page</h1>")

def about(request):
    return HttpResponse("<h1>About Us: We build cloud solutions</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us at: info@example.com</h1>")

def services(request):
    return HttpResponse("<h1>Our Services Include: Web Development, AWS, and CI/CD</h1>")

def portfolio(request):
    return HttpResponse("<h1>Portfolio: See our previous Django and AWS projects</h1>")

def blog(request):
    return HttpResponse("<h1>Blog: Read our latest tech articles</h1>")

def testimonials(request):
    return HttpResponse("<h1>Testimonials: What our clients say</h1>")

def faq(request):
    return HttpResponse("<h1>FAQ: Frequently Asked Questions</h1>")

def pricing(request):
    return HttpResponse("<h1>Pricing Plans: Starter, Pro, and Enterprise</h1>")