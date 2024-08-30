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
    PatientViewSet,
    CityViewSet,
    StateViewSet,
    RaceViewSet,
    EnvironmentViewSet,
    EthnicityViewSet,
    GenderViewSet,
    DistrictViewSet,
    OrderingPhysicianNPIViewSet,
    TestLocationViewSet
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
router.register(r'districts', DistrictViewSet)
router.register(r'test-locations', TestLocationViewSet)
router.register(r'ordering-physicians', OrderingPhysicianNPIViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'cities', CityViewSet)
router.register(r'states', StateViewSet)
router.register(r'races', RaceViewSet)
router.register(r'ethnicities', EthnicityViewSet)
router.register(r'environments', EnvironmentViewSet)
router.register(r'genders', GenderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
