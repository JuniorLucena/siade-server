from django_filters import FilterSet

def AutoFilterSet(queryset, *args, **kwargs):
	_fields = kwargs.get('fields', None)
	class AutoFilterSet(FilterSet):
		class Meta:
			model = queryset.model
			fields = _fields
			order_by = True
	return AutoFilterSet