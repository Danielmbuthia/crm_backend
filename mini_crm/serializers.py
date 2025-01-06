from rest_framework import serializers
from .models import Lead, Contact, Note, Reminder

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all(), write_only=True)
    lead_detail = LeadSerializer(source='lead',read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'

class NoteSerializer(serializers.ModelSerializer):
    lead = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all(), write_only=True)
    lead_detail = LeadSerializer(source='lead',read_only=True)

    class Meta:
        model = Note
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    lead_detail = LeadSerializer(source='lead', read_only=True)
    lead = serializers.PrimaryKeyRelatedField(queryset=Lead.objects.all(), write_only=True)
    

    class Meta:
        model = Reminder
        fields = '__all__'
