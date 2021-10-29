from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from lang_detector import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name="snippets"),
    path('snippets/<str:pk>/', views.SnippetDetail.as_view(), name="snippets-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
