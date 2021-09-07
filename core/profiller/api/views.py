from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil
from profiller.api.serializers import ProfilSeriazlizer

class ProfilList(generics.ListAPIView):
    queryset = Profil.objects.all()
    serializer_class =  ProfilSeriazlizer
    permission_classes = [IsAuthenticated]