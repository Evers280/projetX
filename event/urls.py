from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EventsViewSet, OrganisateursViewSet, InvitesViewSet, TicketsViewSet



# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'events', EventsViewSet, basename='events')
router.register(r'Organisateurs', OrganisateursViewSet, basename='organisateurs')
router.register(r'invites', InvitesViewSet, basename='invites')
router.register(r'tickets', TicketsViewSet, basename='tickets')

urlpatterns = [
    path('', include(router.urls))
]
