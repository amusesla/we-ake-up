from django.urls import path
from .views import LoginView, CeleryView

urlpatterns = [
    path('/login', LoginView.as_view()),
    path('/celery', CeleryView.as_view())
]
