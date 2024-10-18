# urls.py
from django.contrib import admin
from django.urls import path
from app import views  # Ensure to import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hey/<str:name>/', views.hey_you, name='hey_you'),
    path('age-in/<int:end>/<int:birthyear>/', views.age_in, name='age_in'),
    path('order-total/<int:burgers>/<int:fries>/<int:drinks>/', views.order_total, name='order_total'),
]
