from rest_framework import viewsets, mixins, filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Fop, FopRecord
from .serializers import FopSerializer, FopRecordSerializer


class FopViewSet(mixins.ListModelMixin,
                 mixins.RetrieveModelMixin,
                 viewsets.GenericViewSet):
    """
    A ViewSet for viewing Fop data.
    """
    queryset = Fop.objects.all()
    serializer_class = FopSerializer


class FopRecordViewSet(mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       viewsets.GenericViewSet):
    """
    A ViewSet for viewing Fop record data.
    """
    queryset = FopRecord.objects.all()
    serializer_class = FopRecordSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['fio', 'address']
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['stan', 'kved']
