from django.db import models

# Create your models here.

class Eleicao (models.Model):
	nome = models.CharField(max_length=130)
	DHInicio = models.DateTimeField()
	DHFim = models.DateTimeField()

		
class Eleitor(models.Model):
	nome = models.CharField(max_length=200, blank=True, null= False)
	id = models.AutoField(primary_key=True)
	eleicao = models.ForeignKey(Eleicao, null=True, blank=False)
	
class Vagas(models.Model):
	nomeVaga = models.CharField(max_length=200, blank=True, null= False)
	QntVaga = models.IntegerField(blank=True, null= False)

	
class Candidato (models.Model):
	nome = models.CharField(max_length=200, blank=True, null= False)
	chapa = models.CharField(max_length=150, blank=True, null= False)
	numero = models.IntegerField(max_length=3, blank=True, null= False)
	proposta = models.TextField(blank=True, null=False)
	vaga= models.ForeignKey(Vagas, null=True, blank=False)
	
class Tolken (models.Model):
	idTolken = models.AutoField(primary_key=True)
	idEleitor = models.ForeignKey(Eleitor, blank=True, null= False) 
		

class Resultado (models.Model):
	nomeVencendor = models.CharField(max_length=200, blank=True, null= False)
	numeroVencedor = models.IntegerField(max_length=3, blank=True, null= False)
	qntVotos = models.IntegerField(blank=True, null= False)
	qntVotorVencedor = models.IntegerField(blank=True, null= False)
	#qntVotosCandidatos = models.IntegerField(blank=True, null= False)
	#def __str__(self):
       # return "{},{}".format(self.nomeVencendor, self.numeroVencedor)	

class Voto (models.Model):
        candidato= models.ForeignKey(Candidato, null=True, blank=True)
        voto =  models.IntegerField(blank=True, null= False)
        branco = models.BooleanField(default=False, verbose_name="branco")
