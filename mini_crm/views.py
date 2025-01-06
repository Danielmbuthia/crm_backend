
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Lead, Contact, Note, Reminder
from .serializers import LeadSerializer, ContactSerializer, NoteSerializer, ReminderSerializer
from .filters import LeadFilter,ContactFilter,NoteFilter,ReminderFilter

class LeadViewSet(ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = LeadFilter
 

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ContactFilter

class NoteViewSet(ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = NoteFilter

class ReminderViewSet(ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = ReminderFilter
