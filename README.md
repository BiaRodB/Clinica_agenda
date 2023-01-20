# Agenda_clinica
Agenda de uma clinica medica feita em Django, Rest framework 

## Preparando o ambiente
Instale o python;
Instale um IDE - editor de código (vs code, pycharm, etc)
Você pode criar uma pasta normalmente: clicando no botão direito do mause e em seguida clicar em novo e pasta.
Porém você também pode criar pelo terminal usando o seguinte codigo:
```python
mkdir Clinica
```
Após isso, digite:
```python
cd Clinica
```
Criando ambiente virtual para os pacotes do projeto
Essa parte pode ser criado dentro do terminal/ cmd do IDE
Linux:
```python
virtualenv venv
. venv/bin/activate
```
Windows:
```python
pip install virtualenv
python -m venv env
env\Scripts\activate
```
Instalando o Django e e Django REST framework no ambiente virtual:
```python
pip install django
pip install djangorestframework
pip install markdown       
pip install django-filter  
```
Criando o projeto e a aplicação:
```python
django-admin startproject core .  
django-admin startapp agenda
```
Configurando o settings.py: 
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'agenda',
]
```
Ainda no settings.py mudaremos o idioma para português:
```python
LANGUAGE_CODE = 'pt-br'
```
No arquivo clientes/models.py definimos todos os objetos chamados Modelos, tem que apagar tudo dele e escrever o seguinte código:

```python
from django.db import models
from datetime import date, time
from django.utils import timezone
from django.core.exceptions import ValidationError # Esse importe foi usado para validar a data, ele não deixa que a data seja adicionada ao banco de forma errada.

class Especialidade(models.Model): #Especialidade do medico: ortopedia, psiquiatria...
    especialidade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.especialidade

class Cadastrar(models.Model): #Cadastar o médico
    nome = models.CharField(max_length=200)
    crm = models.CharField(max_length=50,unique=True)
    email = models.EmailField(blank=False, max_length=50)
    telefone = models.CharField(max_length=14)
    especialidade = models.ForeignKey(Especialidade,on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return self.nome

def validarData(value): # Data Antiga não poderão ser colocadas, pois criamos esse validador
    hoje = timezone.now().date()
    if value < hoje :
        raise(ValidationError("Data ultrapassada, insira uma data maior ou igual a de hoje"))

class AgendaM(models.Model):
    medico = models.ForeignKey(Cadastrar,on_delete=models.DO_NOTHING)
    data = models.DateField(null=False, validators=[validarData]) # Aqui coloca o nome da def que usamos para validar a data   
    

class Cliente(models.Model): #Cadastro de clientes
    NIVEL = (('F', 'F'),('M', 'M'))
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, max_length=30, )
    cpf = models.CharField(max_length=11, unique=True)
    telefone = models.CharField(max_length=14)
    sexo = models.CharField(max_length=1,choices=NIVEL, blank=False, null=False, default='M')


    def __str__(self):
        return self.nome           

class Consulta(models.Model): #  Marcar a consulta
    Horarios = (
        ("08:00", "08:00 ás 09:00"),
        ("09:00", "09:00 ás 10:00"),
        ("10:00", "10:00 ás 11:00"),
        ("14:00", "14:00 ás 15:00"),
        ("15:00", "15:00 ás 16:00"),
        ("16:00", "16:00 ás 17:00"), )
    
    nomeC = models.CharField(max_length=100)
    especial = models.ForeignKey(Especialidade,on_delete=models.DO_NOTHING)
    med = models.ForeignKey(Cadastrar, on_delete=models.DO_NOTHING) 
    data = models.DateField(null=False, validators=[validarData])
    hora  = models.CharField(max_length=20 , choices=Horarios)
    

    def __str__(self):
        return self.nomeC
```
Em seguida usaremos o comando makemigrations, pois ele analisa se foram feitas mudanças nos modelos e, em caso positivo, cria novas migrações ( Migrations ) para alterar a estrutura do seu banco de dados, refletindo as alterações feitas.
```python
python manage.py makemigrations agenda
```
O Django preparou um arquivo de migração que precisamos aplicar ao nosso banco de dados:
```python
python manage.py migrate agenda 
```
```python
python manage.py migrate 
```

Criar um administrador/ superusuario:
```python
python manage.py createsuperuser
```
"Usuário (leave blank to use 'usuario'):

Endereço de email:

Password:

Password (again):

Superuser created successfully."

Vamos abrir agenda/admin.py no editor de código, apagar tudo dele e escrever o seguinte código:
```python
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
```
vamos criar um arquivo dentro do app chamado serializers.py e adicionar os seguintes códigos:
```python
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

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = '__all__'


class CadastrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cadastrar
        fields = '__all__'
```

Vamos abrir agenda/views.py no editor de código, apagar tudo dele e escrever o seguinte código:

```python
from django.shortcuts import render
from rest_framework import viewsets, permissions
from agenda.serializers import EspecialidadeSerializer, ClienteSerializer, AgendaMSerializer, ConsultaSerializer, CadastrarSerializer
from agenda.models import Cliente, Especialidade, AgendaM, Consulta, Cadastrar

class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AgendaMViewSet(viewsets.ModelViewSet):
    queryset = AgendaM.objects.all()
    serializer_class = AgendaMSerializer
    permission_classes = [permissions.IsAuthenticated]  
      
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
```
O comando 'permission_classes = [permissions.IsAuthenticated]' só deixa editar/adicionar informações se for administrador.

Vamos editar core/urls.py no editor de código:
```python
from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from agenda.views import ClientesViewSet, EspecialidadeViewSet, AgendaMViewSet,ConsultaViewSet, CadastrarViewSet

router = routers.DefaultRouter()
router.register('especialidade',EspecialidadeViewSet)
router.register('cadastrar', CadastrarViewSet)
router.register('agenda', AgendaMViewSet)
router.register('clientes', ClientesViewSet)
router.register('consulta', ConsultaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
```
Vamos startar o servidor web:

```python
python manage.py runserver
```
