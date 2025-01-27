from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from mypet.users.api.views import UserViewSet
from mypet.api.views import (
    CoordinateViewSet,
    CountryViewSet,
    DepartmentViewSet,
    CityViewSet,
    DistrictViewSet,
    TimeZoneViewSet,
    PointViewSet,
    PetTypeViewSet,
    BreedViewSet,
    PetViewSet,
    PetFeaturesViewSet,
    PostViewSet,
    PostImageViewSet,
)

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("coordinate", CoordinateViewSet)
router.register("country", CountryViewSet)
router.register("department", DepartmentViewSet)
router.register("city", CityViewSet)
router.register("district", DistrictViewSet)
router.register("timezone", TimeZoneViewSet)
router.register("point", PointViewSet)
router.register("pet_type", PetTypeViewSet)
router.register("breed", BreedViewSet)
router.register("pet", PetViewSet)
router.register("pet_features", PetFeaturesViewSet)
router.register("post", PostViewSet)
router.register("post_image", PostImageViewSet)

app_name = "api"
urlpatterns = router.urls
