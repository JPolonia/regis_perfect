from django.apps import apps
from django.contrib import admin

from .models import *

admin.site.site_header = "Administração Regis Perfect"
admin.site.site_title = "Portal Regis Perfect"
#admin.site.index_title = "Bem-vindo ao portal Regis Perfect"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(MaleHaircut)
@admin.register(FemaleHaircut)
class HaircutAdmin(admin.ModelAdmin):
    list_display = ['id', 'client', 'date', 'get_professional_name', 'record', 'price_euro']
    list_filter = ['client', 'date']

    def get_professional_name(self, obj):
        return obj.professional.first_name

    get_professional_name.short_description = 'Profissional'
    get_professional_name.admin_order_field = 'professional__first_name'

    def price_euro(self, obj):
        return f'{obj.price} €'

    price_euro.short_description = 'Preço'
    price_euro.admin_order_field = 'price'


models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass
