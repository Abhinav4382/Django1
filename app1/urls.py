from django.urls import path
from . import views
urlpatterns = [
    path('contact/', views.contact_us, name='contact'),
    path('about/', views.about_us, name='about'),
    path('faq/', views.faq, name='faq'),
]
