from django.urls import path
from . import views
from .views import create_checkout_session, item_detail, success, cancel

urlpatterns = [
    path('', views.index),
    path('buy/<int:pk>', create_checkout_session),
    path('item/<int:pk>', item_detail),
    path('success/', success),
    path('cancel/', cancel)
]