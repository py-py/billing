from django.urls import path, include
from project.admin import invoice_admin

urlpatterns = [
    path('admin/', invoice_admin.urls),
    path('api/', include('backend_rest.urls'))
]
