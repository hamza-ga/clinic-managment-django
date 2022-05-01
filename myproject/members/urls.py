from django.urls import path 
from .views import  SignupPatientView , PatientEditView ,PasswordsChangeView #, LoginPatientView #, LoginDoctorView

urlpatterns = [
    path('signup/', SignupPatientView.as_view(), name='signup'),
    path('edit_profile/', PatientEditView.as_view(),name = 'edit_profile'),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'),name = 'change_pass'),

]