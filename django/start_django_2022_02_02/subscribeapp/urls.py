from subscribeapp.views import SubscriptionView

from django.urls import path

app_name = 'subscribeapp'

urlpatterns = [
    path('subscirbe/', SubscriptionView.as_view(), name='subscribe')
]