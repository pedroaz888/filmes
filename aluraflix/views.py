from rest_framework import viewsets, filters
from aluraflix.serializers import ProgramaSerializer
from aluraflix.models import Programa
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ProgramaViewSet(viewsets.ModelViewSet):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['titulo', 'data_lancamento']
    filterset_fields = ['tipo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

