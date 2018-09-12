from django.urls import path
from project.admin import invoice_admin

urlpatterns = [
    path('admin/', invoice_admin.urls),
]
