import django_filters
from .models import Lead, Contact, Note, Reminder

class LeadFilter(django_filters.FilterSet):
    class Meta:
        model = Lead
        fields = {
            'name': ['icontains'],
            'email': ['icontains'],
            'phone': ['icontains'],
        }


class ContactFilter(django_filters.FilterSet):
    class Meta:
        model = Contact
        fields = {
            'name': ['icontains'],
            'email': ['icontains'],
            'phone': ['icontains'],
        }


class NoteFilter(django_filters.FilterSet):
    class Meta:
        model = Note
        fields = {
            'content': ['icontains'],
        }


import django_filters
from django.utils.timezone import now, timedelta
from .models import Reminder


class ReminderFilter(django_filters.FilterSet):
    today = django_filters.BooleanFilter(method='filter_today', label='Today')
    tomorrow = django_filters.BooleanFilter(method='filter_tomorrow', label='Tomorrow')
    this_week = django_filters.BooleanFilter(method='filter_this_week', label='This Week')
    this_month = django_filters.BooleanFilter(method='filter_this_month', label='This Month')
    this_year = django_filters.BooleanFilter(method='filter_this_year', label='This Year')

    reminder_time__gt = django_filters.DateTimeFilter(field_name='reminder_time', lookup_expr='gt', label='Reminder Time (greater than)')

    class Meta:
        model = Reminder
        fields = {
            'message': ['icontains'],
        }

    def filter_today(self, queryset, name, value):
        if value:
            today_start = now().replace(hour=0, minute=0, second=0, microsecond=0)
            today_end = today_start + timedelta(days=1)
            return queryset.filter(reminder_time__range=(today_start, today_end))
        return queryset

    def filter_tomorrow(self, queryset, name, value):
        if value:
            tomorrow_start = now().replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
            tomorrow_end = tomorrow_start + timedelta(days=1)
            return queryset.filter(reminder_time__range=(tomorrow_start, tomorrow_end))
        return queryset

    def filter_this_week(self, queryset, name, value):
        if value:
            today = now()
            week_start = today - timedelta(days=today.weekday())
            week_end = week_start + timedelta(days=7)
            return queryset.filter(reminder_time__range=(week_start, week_end))
        return queryset

    def filter_this_month(self, queryset, name, value):
        if value:
            today = now()
            month_start = today.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
            next_month = (month_start + timedelta(days=31)).replace(day=1)
            return queryset.filter(reminder_time__range=(month_start, next_month))
        return queryset

    def filter_this_year(self, queryset, name, value):
        if value:
            today = now()
            year_start = today.replace(month=1, day=1, hour=0, minute=0, second=0, microsecond=0)
            next_year = year_start.replace(year=year_start.year + 1)
            return queryset.filter(reminder_time__range=(year_start, next_year))
        return queryset

