import django_filters
from django_filters import DateFilter
from .models import *
from django import forms



class TutorialFilter(django_filters.FilterSet):

    # ate_from = django_filters.DateFilter(widget=DateTypeInput(attrs={'value': '1970-01-01'}),
    #                                                          field_name='journal_entry__date',
    #                                                           lookup_expr='gte',
    #                                                           label='From')

    DATE_CHOICES = (
                ('newest', 'Newest'),
                ('oldest', 'Oldest')
    )
    date_sort = django_filters.ChoiceFilter(label   ='Sort by Date ',
                                            choices =DATE_CHOICES,
                                            method  ='filter_by_date',
                                            # widget  =forms.Select(attrs={'size': 4})
                                           )

    class Meta:
        model = TutorialList

        fields = {
            'title'     : ['icontains'],
            'instructor': ['icontains'],
            'language'  : ['exact'],
            'difficulty': ['exact'],
        }



    def filter_by_date(self, queryset, name, value):
        expression = 'last_updated' if value == 'oldest' else '-last_updated'
        return queryset.order_by(expression)

