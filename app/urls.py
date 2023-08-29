
from django.contrib import admin
from django.urls import path
from .views import predict_car

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', predict_car, name='car_predict_input'),
]
