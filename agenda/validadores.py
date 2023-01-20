from agenda.serializers import EspecialidadeSerializer, ClienteSerializer,ConsultaSerializer,AgendaMSerializer
from agenda.models import Especialidade,AgendaM,Cliente,Consulta
import re


def validar_celular(numero_celular):
    modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    resposta = re.findall(modelo, numero_celular)
    return resposta

def validar_cpf(numero_cpf):
    if (len(numero_cpf) != 11):
        return cpf


