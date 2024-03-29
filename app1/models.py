from django.db import models

# Create your models here.

TIPO = (
    (1, 'despesa'),
    (2, 'receita')
)

class Emissor(models.Model):
    '''
    Modelo representa o Emissor da Nota Fiscal
    O Emissor é uma empresa que emite a nota fiscal para que eu a pague, ou, minha empresa emite uma nota fiscal.
    '''
    cnpj = models.CharField('CNPJ', max_length=50, primary_key=True)
    nome = models.CharField('nome', max_length=50)

    def __str__(self):

        return str(self.cnpj)


class Lancamento(models.Model):

    num_nota_fiscal = models.CharField('numero da nota fiscal', max_length=50, blank=True, null=True)
    receita_despesa = models.PositiveSmallIntegerField('receita ou despesa', choices=TIPO)  # True = Receita

    emissor = models.ForeignKey(Emissor, blank=True, null=True, on_delete=models.CASCADE)

    valor_nota = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    desconto = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'Lançamento'
        verbose_name_plural = 'Lançamentos'

    def __str__(self):

        return str(self.pk)