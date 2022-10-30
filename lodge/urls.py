from django.urls import path
from . import views

# http://127.0.0.1:8000/
# http://127.0.0.1:8000/account
# http://127.0.0.1:8000/about


urlpatterns = [
    path("index.html", views.home),
    path("about.html", views.about,),
    path("jewellery.html", views.jewellery),
    path("contact.html", views.contact)
]