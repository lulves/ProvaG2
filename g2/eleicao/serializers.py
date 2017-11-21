from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from eleicao.views import *

class EleicaoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eleicao
        fields = ('nome','DHInicio', 'DHFim',)
    def create(self, validated_data):
        eleicao_data = Eleicao.objects.create(**validated_data)
        return eleicao_data

class EleitorSerializer (serializers.HyperlinkedModelSerializer):
    #faixaHr = FaixaHorariaSerializer(many='False')
    class Meta:
        model = Eleitor
        fields = ('nome', 'id', )
    def create(self, validated_data):
        eleitor_data = Eleitor.objects.create(**validated_data)
        return eleitor_data

class VagasSerializer (serializers.HyperlinkedModelSerializer):
    #funcionarios = FuncionarioSerializer(many='False')
    class Meta:
        model = Vagas
        fields = ('nomeVaga', 'QntVaga',)
    def create(self, validated_data):
        vagas_data = Vagas.objects.create(**validated_data)
        return vagas_data

class CandidatoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidato
        fields = ('nome','chapa', 'numero','proposta')
    def create(self, validated_data):
        candidato_data = Candidato.objects.create(**validated_data)
        return candidato_data

class TolkenSerializer (serializers.HyperlinkedModelSerializer):
	idEleitor = EleicaoSerializer(many=False)
    class Meta:
	model = Tolken
	fields = ('idTolken', 'idEleitor')
    def create(self, validated_data):
        tolken_data = Tolken.objects.create(**validated_data)
        return tolken_data
	
class ResultadoSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
	model= Resultado
	fields = ('nomeVencedor', 'numeroVencedor', 'qntVagas', 'qntVencedor',)

class VotoSerializer (serializers.HyperlinkedModelSerializer):
	candidato = CandidatoSerializer(many=False)
    class Meta:
	model= Voto
	fields = ('candidato', )
