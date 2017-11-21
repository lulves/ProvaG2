from django.shortcuts import render
from django.http import HttpResponse
from eleicao.models import *
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eleicao.serializers import *
# Create your views here.
class EleicaoViewSet(viewsets.ModelViewSet):
    queryset = Eleicao.objects.all()
    serializer_class = EleicaoSerializer

class EleitorViewSet(viewsets.ModelViewSet):
    queryset = Eleitor.objects.all()
    serializer_class = EleitorSerializer

class VagasViewSet(viewsets.ModelViewSet):
    queryset = Vagas.objects.all()
    serializer_class = VagasSerializer

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer

class TolkenViewSet(viewsets.ModelViewSet):
    queryset = Tolken.objects.all()
    serializer_class = TolkenSerializer
	
class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoSerializer

class VotoViewSet(viewsets.ModelViewSet):
    queryset = Voto.objects.all()
    serializer_class = VotoSerializer