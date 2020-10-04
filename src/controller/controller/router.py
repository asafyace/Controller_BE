from core.api.viewsets import ServerViewSet, LabViewSet, UserViewSet, ComplainViewSet, CommandViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('Lab', LabViewSet)
router.register('Server', ServerViewSet)
router.register('User', UserViewSet)
router.register('Complain', ComplainViewSet)
router.register('Command', CommandViewSet)
