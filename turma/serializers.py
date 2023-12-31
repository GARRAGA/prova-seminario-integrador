from .models import Turma
from rest_framework import serializers


class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = [
            'codigoturma',
            'codigocurso'
        ]
