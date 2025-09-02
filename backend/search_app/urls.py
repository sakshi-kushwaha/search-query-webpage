from django.urls import path
from .views import SearchView, HealthCheckView

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('health/', HealthCheckView.as_view(), name='health'),
] 