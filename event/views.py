from rest_framework import viewsets
from .models import Events, Organisateurs, Invites, Tickets
from .serializers import EventsSerializers, OrganisateursSerializers, InvitesSerializers, TicketsSerializers

# Create your views here.
class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers
    

class OrganisateursViewSet(viewsets.ModelViewSet):
    queryset = Organisateurs.objects.all()
    serializer_class = OrganisateursSerializers 
       
       
class InvitesViewSet(viewsets.ModelViewSet):
    queryset = Invites.objects.all()
    serializer_class = InvitesSerializers
    
    
class TicketsViewSet(viewsets.ModelViewSet):
    queryset = Tickets.objects.all()
    serializer_class = TicketsSerializers           