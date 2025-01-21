from django.shortcuts import render
def contact_us(request):
    return render(request, 'contact_us.html')

def about_us(request):
    return render(request, 'about_us.html')

def faq(request):
    return render(request, 'faq.html')