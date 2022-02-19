from django.urls import path
from . import views

urlpatterns = [
    path('cover',views.getcover),
    path('headset',views.getheadset)

]
