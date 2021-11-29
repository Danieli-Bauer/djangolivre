import math
from django.db import models
import random

class Conta(models.Model):
    agencia = models.CharField(max_length=5)
    numero_conta = models.CharField(max_length=10)
    saldo = models.CharField(max_length=20)
    saldo_inicial = 500.00


    def __str__(self) -> int():
        return self.numero_conta

    def gera_conta():
        return math.ceil(100000 * random.random())

    print(gera_conta())
