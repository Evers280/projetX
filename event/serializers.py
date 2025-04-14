from .models import Events, Organisateurs, Invites, Tickets
from rest_framework import serializers


class EventsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'
        
        

class OrganisateursSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Organisateurs
        fields = '__all__'   
        
        

class InvitesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invites 
        fields = '__all__' 
        


class TicketsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tickets
        fields = '__all__'                   