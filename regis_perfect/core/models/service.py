from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .choices import *


class Client(models.Model):
    SEX = [
        ('m', 'Masculino'),
        ('f', 'Feminino'),
    ]

    name = models.CharField(_('Nome'), max_length=50)
    sex = models.CharField(_('Sexo'), max_length=1, choices=SEX)
    birth_date = models.DateField(_('Data de nascimento'), blank=True, null=True)
    email = models.CharField(_('Email'), max_length=30, blank=True, null=True)
    referral = models.CharField(_('Como nos conheceu'), max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        # app_label = 'auth'

# class ServiceType(models.Model):
#     name = models.CharField(_('Nome'), max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Tipo de serviço'
#         verbose_name_plural = 'Tipos de serviço'
#
#
# class ServiceCategory(models.Model):
#     service_type = models.ForeignKey('ServiceType', on_delete=models.PROTECT)
#     name = models.CharField(_('Nome'), max_length=10, unique=True)
#
#     class Meta:
#         verbose_name = 'Categoria'
#         verbose_name_plural = 'Categorias'

class Service(models.Model):
    TYPE = [
        ('m', 'Corte Masculino'),
        ('f', 'Corte Femino'),
        ('t', 'Técnico'),
        ('e', 'Estética'),
        ('l', 'Lazer'),
    ]

    client = models.ForeignKey(Client, verbose_name='Cliente', on_delete=models.PROTECT)
    professional = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    date = models.DateTimeField(_('Data'), default=timezone.now)
    price = models.IntegerField(_('Valor do serviço'))
    record = models.TextField(_('Registo'), null=True, blank=True)
    # type = models.CharField(_('Tipo'), max_length=1, choices=TYPE)
    # type = models.ForeignKey('ServiceType', verbose_name=_('Tipo de serviço'), on_delete=models.PROTECT)

    # Corte Masculino
    # laterals = models

    class Meta:
        abstract = True
        #verbose_name = 'Serviço'
        #verbose_name_plural = 'Serviços'



class MaleHaircut(Service):
    laterals = models.ForeignKey(Laterals, verbose_name=_('Laterais'), on_delete=models.PROTECT, null=True, blank=True)
    top = models.ForeignKey(Top, verbose_name=_('Topo'), on_delete=models.PROTECT, null=True, blank=True)
    top_technique = models.ForeignKey(TopTechnique, verbose_name=_('Topo técnica'), on_delete=models.PROTECT, null=True, blank=True)

    hairstyle = models.ForeignKey(HairStyle, verbose_name=_('Penteado'), on_delete=models.PROTECT, null=True, blank=True)
    beard = models.ForeignKey(Beard, verbose_name=_('Barba'), on_delete=models.PROTECT, null=True, blank=True)

    # Technical services
    coloring = models.ForeignKey(Coloring, verbose_name=_('Coloração'), on_delete=models.PROTECT, null=True, blank=True)
    locks = models.ForeignKey(Locks, verbose_name=_('Madeixas'), on_delete=models.PROTECT, null=True, blank=True)
    straightening = models.ForeignKey(Straightening, verbose_name=_('Alisamento'), on_delete=models.PROTECT, null=True, blank=True)

    class Meta:
        verbose_name = _('Corte Masculino')
        verbose_name_plural = _('Corte Masculino')

class FemaleHaircut(Service):
    '''tipo de corte - pontas danificadas, bob, long bob, escadeado, muito escadeado, inteiro, recto, +
    tamanho - muito curto, linha orelha, linha pescoço, linha ombros, baixo ombros, linha omoplata, abaixo omoplata, +
    franja - direção (direita, esquerda, frente, +).
    tamanho (longa, linha sobrancelha, cima sobrancelha, linha do nariz, linha do queixo, +)
    '''
    haircut_type = models.ForeignKey(HaircutType, verbose_name=_('Tipo de corte'), on_delete=models.PROTECT, null=True, blank=True)
    haircut_size = models.ForeignKey(HaircutSize, verbose_name=_('Tamanho do corte'), on_delete=models.PROTECT, null=True, blank=True)
    bangs = models.ForeignKey(Bangs, verbose_name=_('Franja'), on_delete=models.PROTECT, null=True, blank=True)
    bangs_size = models.ForeignKey(BangsSize, verbose_name=_('Tamanho da franja'), on_delete=models.PROTECT, null=True, blank=True)


    class Meta:
        verbose_name = _('Corte Feminino')
        verbose_name_plural = _('Corte Feminino')
