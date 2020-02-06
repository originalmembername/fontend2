from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Vocabs
from .serializers import VocabsSerializer

# tests for views


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_vocab(german="", english=""):
        if german != "" and english != "":
            Vocabs.objects.create(german=german, english=english)

    def setUp(self):
        # add test data
        self.create_vocab("laufen", "run")
        self.create_vocab("Hund", "dog")
        self.create_vocab("spielen", "play")
        self.create_vocab("kalt", "cold")


class GetAllVocabsTest(BaseViewTest):

    def test_get_all_vocabs(self):
        """
        This test ensures that all vocabs added in the setUp method
        exist when we make a GET request to the vocabs/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("vocabs-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Vocabs.objects.all()
        serialized = VocabsSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class ImgStoreTest(BaseViewTest):

    # def test_download_img_from_url(self)
    """
    This test downloads an image from an url to the server
    """

# Create your tests here.

