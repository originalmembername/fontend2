from django.urls import path
from .views import ListPersonalVocabsView


urlpatterns = [
    path('vocabs/personal/', ListPersonalVocabsView.as_view(), name="vocabs-personal")
]