from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    RegisterSerializer, LoginSerializer, PatientSerializer,
    DoctorSerializer, MappingSerializer
)
from .models import Patient, Doctor, PatientDoctorMapping

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

class PatientListCreateView(generics.ListCreateAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = MappingSerializer
    permission_classes = [IsAuthenticated]

class MappingDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        patient = get_object_or_404(Patient, pk=pk)
        if patient.user != request.user:
            raise PermissionDenied("Not your patient")
        doctors = Doctor.objects.filter(patients__patient=patient)
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)

    def delete(self, request, pk):
        mapping = get_object_or_404(PatientDoctorMapping, pk=pk)
        if mapping.patient.user != request.user:
            raise PermissionDenied("Not your patient")
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)