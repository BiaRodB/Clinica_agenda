from django.shortcuts import render
from rest_framework import viewsets, permissions
from agenda.serializers import EspecialidadeSerializer, ClienteSerializer, AgendaMSerializer, ConsultaSerializer, CadastrarSerializer
from agenda.models import Cliente, Especialidade, AgendaM, Consulta, Cadastrar
from datetime import date

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgendaMViewSet(viewsets.ModelViewSet):
    queryset = AgendaM.objects.all()
    serializer_class = AgendaMSerializer
    permission_classes = [permissions.IsAuthenticated]  

    def validate_date(value):
        hoje = date.today()
        datas = AgendaM('__data__')    
        if datas < hoje :
           return ValidationError(" msg de erro")
      
class ClientesViewSet(viewsets.ModelViewSet):
    """Listando clientes"""
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer


class CadastrarViewSet(viewsets.ModelViewSet):
    queryset = Cadastrar.objects.all()
    serializer_class = CadastrarSerializer
    permission_classes = [permissions.IsAuthenticated]