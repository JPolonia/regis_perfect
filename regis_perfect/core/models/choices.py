from django.db import models
from django.utils.translation import gettext_lazy as _


class Choice(models.Model):
    value = models.CharField(_('Valor'), max_length=50)

    def __str__(self):
        return self.value

    class Meta:
        abstract = True


# Corte Masculino
class CutType(Choice):
    class Meta:
        verbose_name = _('Tipo de corte')
        verbose_name_plural = _('Tipos de corte')


class Laterals(Choice):
    type = models.ForeignKey(CutType, verbose_name='Tipo', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.type} - {self.value}'

    class Meta:
        verbose_name = _('Laterais')
        verbose_name_plural = _('Tipos de Laterais')


class Top(Choice):
    type = models.ForeignKey(CutType, verbose_name='Tipo', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.type} - {self.value}'

    class Meta:
        verbose_name = _('Laterais')
        verbose_name_plural = _('Tipos de laterais')


class TopTechnique(Choice):
    class Meta:
        verbose_name = _('Topo técnica')
        verbose_name_plural = _('Técnicas de topo')


class HairStyle(Choice):
    class Meta:
        verbose_name = _('Penteado')
        verbose_name_plural = _('Tipos de penteado')


class Beard(Choice):
    class Meta:
        verbose_name = _('Barba')
        verbose_name_plural = _('Tipos de barba')


class Coloring(Choice):
    class Meta:
        verbose_name = _('Coloração')
        verbose_name_plural = _('Tipos de coloração')


class Locks(Choice):
    class Meta:
        verbose_name = _('Madeixas')
        verbose_name_plural = _('Tipos de madeixa')


class Straightening(Choice):
    class Meta:
        verbose_name = _('Alisamento')
        verbose_name_plural = _('Tipos de alisamento')


# Female Haircut
class HaircutType(Choice):
    class Meta:
        verbose_name = _('Tipo de corte')
        verbose_name_plural = _('Tipos de corte')


class HaircutSize(Choice):
    class Meta:
        verbose_name = _('Tamanho de corte')
        verbose_name_plural = _('Tamanhos de corte')


class Bangs(Choice):
    class Meta:
        verbose_name = _('Franja')
        verbose_name_plural = _('Tipos de franja')


class BangsSize(Choice):
    class Meta:
        verbose_name = _('Tamanho da franja')
        verbose_name_plural = _('Tamanhos da franja')
