from django.db import models

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100, blank=False)
    nome_social = models.CharField(max_length=100, blank=True)
    telefone = models.CharField(max_length=16, blank=False)
    email = models.EmailField(blank=False)
    cpf = models.CharField(max_length=11, unique=True, blank=False)
    salario = models.DecimalField(max_digits=11, decimal_places=2, blank=False)
    cargo = models.CharField(max_length=50, blank=False)



