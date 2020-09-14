from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('/url_checker/', views.UrlCheckerDetail.as_view()),
    path('/url_checker/<int:pk>/', views.UrlCheckerDetail.as_view()),
    path('url_checker/add/', views.UrlCheckerDetail.as_view()),
    path('url_checker/list/', views.UserViewSet.as_view({'get': 'list'})),
]

urlpatterns = format_suffix_patterns(urlpatterns)