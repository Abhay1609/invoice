from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet,InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoices_detail', InvoiceDetailViewSet)

urlpatterns = router.urls
