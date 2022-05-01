from django.urls import path 
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('dentistry/', views.getDentistryInfo ,name = 'getDentistryInfo'),
    path('dermatology/', views.getDermatologyInfo ,name = 'getDermatologyInfo'),
    path('neurologist/', views.getNeurologistInfo ,name = 'getNeurologistInfo'),
    path('addconsultation/<int:pk>/', views.AddConsultation.as_view() ,name = 'addconsultation'),
    path('sucess/', views.sucess , name = 'sucess'),
    path('show-consults/<int:pk>/', views.ShowConsultsView.as_view() , name = 'showconsults'),
    path('show-consult/<int:pk>/', views.ShowConsultView.as_view() , name = 'showconsult'),
    path('prescription-medicine/<int:pk>/', views.WritePrescriptionView.as_view() , name = 'prescription-medicine'),
    path('show-prescriptionlist/<int:pk>/', views.ShowPrescriptionList.as_view() , name = 'show-prescriptionlist'),
    path('show-prescription/<int:pk>/', views.ShowPrescription.as_view() , name = 'show-prescription'),
    path('pre-consults-view/<int:pk>/', views.ShowPreConsult.as_view() , name = 'pre-consults-view'),
    path('show-pre-consults/<int:pk>/', views.ShowPreConsultsView.as_view() , name = 'showpreconsults'),
    path('show-pre-consult/<int:pk>/', views.ShowPreConsultView.as_view() , name = 'showpreconsult'),
]