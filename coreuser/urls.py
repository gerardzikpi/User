from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.CoreUserViewset,basename="coreuser"),
# router.register(r"create",views.CreateCoreUser, basename = "signup"),


urlpatterns = router.urls