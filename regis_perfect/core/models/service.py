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


class Aesthetics(Service):
    '''
    tipo de serviço - epilação cera,  tratamento de corpo, tratamentos de rosto, pedicure/manicure,
    epilação - produto/cera ( fria, quente, chocolate…), zonas tratadas perna, virilha, buço ...
    massagem- (relaxamento ou terapêutica, anti celulitica, linfática, +)
    tratamentos de rosto- tratamento(limpeza de pele, piling…)
    tipo de pele ( oleosa, normal, mista, seca, acneica…)
    tratamentos de corpo -tratamento( esfoliação, envolvimentos.) tipo de pele(seca, oleosa ou normal)
    manicure/pedicure- serviço (verniz gel,manicure…), produto (gel, verniz gel, acrílico), número/ nome cor
    campo para observações escritas em tratamentos para colocar os produtos e técnicas usadas
    '''
    type = models.ForeignKey(AestheticsType, verbose_name=_('Tipo de serviço'), on_delete=models.PROTECT, null=True, blank=True)
    epilation_product = models.ForeignKey(EpilationProduct, verbose_name=_('Epilação produto'), on_delete=models.PROTECT, null=True, blank=True)
    epilation_zones = models.ForeignKey(EpilationZones, verbose_name=_('Epilação zonas tratadas'), on_delete=models.PROTECT, null=True, blank=True)
    massage = models.ForeignKey(Massage, verbose_name=_('Massagem'), on_delete=models.PROTECT, null=True, blank=True)
    skin_type = models.ForeignKey(SkinType, verbose_name=_('Tipo de pele'), on_delete=models.PROTECT, null=True, blank=True)
    body_treatment = models.ForeignKey(BodyTreatment, verbose_name=_('Tratamentos de corpo'), on_delete=models.PROTECT, null=True, blank=True)
    manicure_service = models.ForeignKey(ManicureService, verbose_name=_('Manicure serviço'), on_delete=models.PROTECT, null=True, blank=True)
    manicure_product = models.ForeignKey(ManicureProduct, verbose_name=_('Manicure produto'), on_delete=models.PROTECT, null=True, blank=True)
    manicure_color = models.ForeignKey(ManicureColor, verbose_name=_('Manicure cor'), on_delete=models.PROTECT, null=True, blank=True)
    pedicure_service = models.ForeignKey(ManicureService, verbose_name=_('Pedicure serviço'), on_delete=models.PROTECT, related_name='pedicure', null=True, blank=True)
    pedicure_product = models.ForeignKey(ManicureProduct, verbose_name=_('Pedicure produto'), on_delete=models.PROTECT, related_name='pedicure', null=True, blank=True)
    pedicure_color = models.ForeignKey(ManicureColor, verbose_name=_('Pedicure cor'), on_delete=models.PROTECT, related_name='pedicure', null=True, blank=True)
    obs = models.TextField(_('Observações'), null=True, blank=True)


    class Meta:
        verbose_name = _('Estética e Manicure')
        verbose_name_plural = _('Estética e Manicure')
