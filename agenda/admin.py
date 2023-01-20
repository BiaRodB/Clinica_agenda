from django.contrib import admin
from agenda.models import AgendaM, Consulta, Especialidade, Cliente,Cadastrar
# Register your models here.
class Agendas(admin.ModelAdmin):
    list_display = ('id', 'medico', 'data',)
    list_display_links = ('id', 'medico',)
    search_fields = ('medico',)
    list_filter = ('data', )
    #list_editable = ('data','horario',)
    list_per_page = 25
    ordering = ('medico',)

admin.site.register(AgendaM, Agendas)

class Consultas(admin.ModelAdmin):
    list_display = ('id','nomeC','especial', 'med','data','hora',)
    list_display_links = ('id','nomeC','data','hora',)
    search_fields = ('nomeC',)
    list_filter = ('nomeC','data', 'hora',)
    #list_editable = ('data','hora',)
    list_per_page = 25
    ordering = ('nomeC',)

admin.site.register(Consulta, Consultas)