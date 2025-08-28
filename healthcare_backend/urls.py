from django.contrib import admin
from django.urls import path
from api.views import (
    RegisterView, LoginView, PatientListCreateView, PatientDetailView,
    DoctorListCreateView, DoctorDetailView, MappingListCreateView, MappingDetailView
)
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/patients/', PatientListCreateView.as_view(), name='patients_list_create'),
    path('api/patients/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('api/doctors/', DoctorListCreateView.as_view(), name='doctors_list_create'),
    path('api/doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('api/mappings/', MappingListCreateView.as_view(), name='mappings_list_create'),
    path('api/mappings/<int:pk>/', MappingDetailView.as_view(), name='mapping_detail'),
]