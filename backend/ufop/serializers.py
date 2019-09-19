from rest_framework import serializers

from .models import Fop, FopRecord


class FopRecordStanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FopRecord
        fields = ['stan']


class FopRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = FopRecord
        fields = ['id', 'fio', 'address', 'kved', 'stan']


class FopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fop
        fields = ['id', 'updated', 'update_date']

