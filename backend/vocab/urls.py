from django.urls import path
from .views import ListVocabsView


urlpatterns = [
    path('vocabs/', ListVocabsView.as_view(), name="vocabs-all")
]