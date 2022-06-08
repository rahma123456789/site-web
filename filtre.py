
import django_filters

from .models import Article2, Temp
class ArticleFiltre(django_filters.FilterSet):

    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Article2
        fields = ['code_famille', 'des_art','cod_art','oem','equivalence']

