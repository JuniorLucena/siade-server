from django_filters import FilterSet

def AutoFilterSet(queryset, filter_fields=None):
	class AutoFilterSet(FilterSet):
		class Meta:
			model = queryset.model
			fields = filter_fields
			order_by = True
	return AutoFilterSet