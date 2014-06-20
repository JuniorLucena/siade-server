from rest_framework import serializers
from siade.imoveis.models import *
from siade.trabalhos.models import *

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
	"""
	A ModelSerializer that takes an additional `fields` argument that
	controls which fields should be displayed.
	"""

	def __init__(self, *args, **kwargs):
		# Instantiate the superclass normally
		super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

		fields = self.context['request'].QUERY_PARAMS.get('fields')
		if fields:
			fields = fields.split(',')
			# Drop any fields that are not specified in the `fields` argument.
			allowed = set(fields)
			existing = set(self.fields.keys())
			for field_name in existing - allowed:
				self.fields.pop(field_name)

def SerializerForModel(model_class, *args, **kwargs):
	_fields = kwargs.get('fields', None)
	_depth = kwargs.get('depth', 0)
	class Serializer(DynamicFieldsModelSerializer):
		class Meta:
			model = model_class
			fields = _fields
			depth = _depth
	return Serializer

class LadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = LadoQuadra
		fields = ('logradouro', 'numero')

class QuadraSerializer(serializers.ModelSerializer):
	lados = LadoSerializer(many=True, allow_add_remove=True)
	class Meta:
		model = Quadra
		fields = ('id', 'numero', 'bairro', 'lados')
		depth = 1

ImovelSerializer = SerializerForModel(Imovel)
VisitaSerializer = SerializerForModel(Visita)