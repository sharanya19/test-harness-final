from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    OrderViewSet, 
    SpecimenViewSet, 
    SpecimenTypeViewSet,
    SpecimenTypeSNOMEDCodeViewSet,
    SourceDescriptionViewSet,
    SpecimenSourceViewSet,
    SourceSNOMEDCodeViewSet,
    SubmitterViewSet, 
    PatientViewSet
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'specimens', SpecimenViewSet)
router.register(r'specimen-types', SpecimenTypeViewSet)
router.register(r'specimen-type-snomed-codes', SpecimenTypeSNOMEDCodeViewSet)
router.register(r'source-descriptions', SourceDescriptionViewSet)
router.register(r'specimen-sources', SpecimenSourceViewSet)
router.register(r'source-snomed-codes', SourceSNOMEDCodeViewSet)
router.register(r'submissions', SubmitterViewSet)
router.register(r'patients', PatientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
