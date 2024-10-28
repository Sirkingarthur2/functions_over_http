from django.contrib import admin
from django.urls import path

from app.views import hey_you
from app.views import age_in
from app.views import order_total

urlpatterns = [
    path('hey/<name>', hey_you),
    path('age-in/<this>/<that>', age_in),
    path('order-total/<burgers>/<fries>/<drinks>', order_total),
    path('admin/', admin.site.urls),
]