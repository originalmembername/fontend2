from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from urllib3 import response

#pylint: disable=relative-beyond-top-level
from .models import Vocabs
from .serializers import VocabsSerializer


class ListPersonalVocabsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = VocabsSerializer

    def get_queryset(self):
        user = self.request.user
        return user.profile.vocab_list

    # Add-function
    #pylint: disable=unused-argument
    def post(self, request, version):
        profile = self.request.user.profile
        # Check if vocab exists in user's vocab list
        if profile.vocab_list.filter(german=request.data['german']).count() == 0:
            vocab = Vocabs.create_vocab(
                german=request.data['german'], english=request.data['english'], picture_url=request.data['imgUrl']
            )
 #           vocab.save() #necessary?
            profile.vocab_list.add(vocab)
            return JsonResponse({'inserted': 'True'})
        else:
            return JsonResponse({'inserted': 'False'})

    def delete(self, request, version):
        profile = self.request.user.profile
        items = request.data['items']
        if len(items) > 0:
            for vocab in items:
                profile.vocab_list.filter(german=vocab).delete()
            return JsonResponse({'deleted': 'True'})
        else:
            return JsonResponse({'deleted': 'False'})

    # Edit-function
    #pylint: disable=unused-argument
    def put(self, request, version):
        profile = self.request.user.profile
        key = request.data['germanOld']
        german = request.data['german']
        english = request.data['english']
        pictureUrl = request.data['imgUrl']
        if key == german:
            # Only update English
            vocabObj = profile.vocab_list.get(german=key)
            vocabObj.english = english
            vocabObj.set_picture(pictureUrl)
            vocabObj.save()
            return JsonResponse({'edited': 'True'})
        elif profile.vocab_list.filter(german=german).count() > 0:
            # Duplicate
            return JsonResponse({'edited': 'False'})
        else:
            # Update german & english
            vocabObj = profile.vocab_list.get(german=key)
            vocabObj.german = german
            vocabObj.english = english
            vocabObj.set_picture(pictureUrl)
            vocabObj.save()
            return JsonResponse({'edited': 'True'})


class ImgTestView(APIView):

    #pylint: disable=unused-argument
    def post(self, clientRequest, version):
        imgUrl = clientRequest.data['imgUrl']
        german = clientRequest.data['german']
        english = clientRequest.data['english']
        vocab = Vocabs.create_vocab(
            german=german, english=english, picture_url=imgUrl)
        serialiser = VocabsSerializer(vocab)
        domain = clientRequest.get_host()
        image = "http://" + domain + serialiser.data['picture']

#        return HttpResponse(vocab.picture, content_type="image/jpeg")
        return JsonResponse({'image': image})
