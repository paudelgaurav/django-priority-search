from django.db.models import Q, Case, When

from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.serializers import ModelSerializer
from django_filters import rest_framework as filters

from .models import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductFilterSet(filters.FilterSet):
    search = filters.CharFilter(method="filter_by_search")

    class Meta:
        model = Product
        fields = ()

    def filter_by_search(self, queryset, name, value):
        """
        title > description > note
        """
        if not value:
            return queryset

        queryset = queryset.filter(
            Q(title__icontains=value)
            | Q(description__icontains=value)
            | Q(note__icontains=value)
        ).annotate(
            search_priority=Case(
                When(Q(title__icontains=value), then=3),
                When(
                    Q(description__icontains=value) & ~Q(title__icontains=value),
                    then=2,
                ),
                When(
                    (Q(note__icontains=value) & ~Q(title__icontains=value))
                    & (Q(note__icontains=value) & ~Q(description__icontains=value)),
                    then=1,
                ),
                default=0,
            ),
        )

        # Ordering the filtered queryset according to their search priority
        return queryset.order_by("-search_priority")


class ProductReadOnlyViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ProductFilterSet
