from .views import home, contact_form_view
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact_form_view, name='contact'),
]