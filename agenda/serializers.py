from rest_framework import serializers
from agenda.models import Especialidade, AgendaM, Cliente, Consulta, Cadastrar
from datetime import date
from django.utils.dateparse import parse_date 
class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'


class AgendaMSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgendaM
        fields = '__all__'
                                  
     
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

"""    def validar_cpf(self, cpf):
        if(len(cpf) != 11):
            raise serealizers.ValidationError("O cpf deve ter 11 dígitos")
        return cpf
    
    def validar_nome(self, nome):
        if not nome.isalpha():
            raise serealizers.ValidationError("Não inclua números neste campo")
        return nome 

    def validar_celular(self, telefone):
        if(len(telefone) < 11):
            raise serealizers.ValidationError("O celular deve ter no mínimo 11 dígitos")
        return telefone
  """  

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class CadastrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastrar
        fields = '__all__'

    """def validar_crm(self, crm):
        if(len(crm) != 8):
            raise serealizers.ValidationError("O CRM deve ter 8 dígitos, incluindo a sigla do estado")
        return crm
    
    def validar_nome(self, nome):
        if not nome.isalpha():
            raise serealizers.ValidationError("Não inclua números neste campo")
        return nome 

    def validar_celular(self, telefone):
        if(len(telefone) < 11):
            raise serealizers.ValidationError("O celular deve ter no mínimo 11 dígitos")
        return telefone
"""