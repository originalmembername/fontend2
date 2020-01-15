from django.urls import path
from .views import ListPersonalVocabsView
from .views import ImgTestView


urlpatterns = [
    path('vocabs/personal/', ListPersonalVocabsView.as_view(), name="vocabs-personal"),
    path('vocabs/imgtest/', ImgTestView.as_view(), name="image-test")
]