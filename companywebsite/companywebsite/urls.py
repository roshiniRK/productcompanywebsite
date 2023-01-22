
from django.contrib import admin
from django.urls import path

from product import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.company,name="company"),
    path("products.html",views.products,name='products'),
    path("home.html", views.company),
    path("people.html",views.people),
    path("contact.html",views.contact),
]
