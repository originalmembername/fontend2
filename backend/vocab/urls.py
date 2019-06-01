from django.urls import path
from .views import ListVocabsView, ListPersonalVocabsView


urlpatterns = [
    path('vocabs/', ListVocabsView.as_view(), name="vocabs-all"),
    path('vocabs/personal/', ListPersonalVocabsView.as_view(), name="vocabs-personal")
]