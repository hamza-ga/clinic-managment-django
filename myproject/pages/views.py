from django.shortcuts import get_list_or_404, render , get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView , DetailView
from members.models import Doctor, Patient, Specialties
from pages.forms import ConsaltationsForm ,PrescriptionForm
from .models import Consaltations , Prescription
# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

class CreatePreConsult():
    pass

class ShowPreConsult(ListView):#patient view
    model = Prescription
    template_name = 'pages/showpreconsultation.html'

class ShowPrescription(DetailView):
    model = Prescription
    template_name = 'pages/showprescription.html'

    # def get_context_data(self, **kwargs):
    #     prescription = get_object_or_404(Prescription, doctor_name= self.kwargs['pk'])
    #     context = super(WritePrescriptionView, self).get_context_data(**kwargs)
    #     context['prescription'] = prescription
    #     return context



class ShowPrescriptionList(ListView):
    model = Prescription
    template_name = 'pages/showprescriptionlist.html'


class WritePrescriptionView(CreateView):
    model = Prescription
    form_class =  PrescriptionForm
    #fields = ('doctor_name','patient_name','body')
    template_name = 'pages/createprescript.html'
    success_url = reverse_lazy('sucess')

    def get_context_data(self, **kwargs):
        consult = get_object_or_404(Consaltations, id= self.kwargs['pk'])
        context = super(WritePrescriptionView, self).get_context_data(**kwargs)
        context['patient_name'] = consult.patient.pk
        context['consult_id'] = consult.pk
        return context



class ShowConsultsView(ListView):#doctor view
    model = Consaltations
    template_name = 'pages/showconsultslist.html'

    def get_context_data(self, **kwargs):
        consults = get_list_or_404(Consaltations, doctor= self.kwargs['pk'])
        context = super(ShowConsultsView, self).get_context_data(**kwargs)
        context['consults'] = consults
        return context   

class ShowConsultView(DetailView):#doctor view
    model = Consaltations
    template_name = 'pages/showconsultlist.html'



class ShowPreConsultsView(ListView):#doctor view
    model = Consaltations
    template_name = 'pages/showpreconsultslist.html'

    def get_context_data(self, **kwargs):
        consults = get_list_or_404(Consaltations, doctor= self.kwargs['pk'])
        context = super(ShowPreConsultsView, self).get_context_data(**kwargs)
        context['consults'] = consults
        return context   

class ShowPreConsultView(DetailView):#doctor view
    model = Consaltations
    template_name = 'pages/showpreconsultlist.html'



def getDentistryInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 3)
    name = 'Dentistry'
    context = {'dok_info': dok_info, 'spcilizname' : name}
    return render(request, 'pages/spetializations_doctor.html', context)



def getDermatologyInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 2)
    name = 'Dermatology'
    context = {'dok_info': dok_info, 'spcilizname':name}
    return render(request, 'pages/spetializations_doctor.html', context)

    def get_context_data(self, *args, **kwargs):
        context = super(Consultation , self).get_context_data(*args,**kwargs)
        doctor_id = get_object_or_404(Doctor, id = self.kwargs['pk'])
        context['doctor_id'] = doctor_id


def getNeurologistInfo(request):
    dok_info = Doctor.objects.filter(spcialty = 1)
    name ='Neurologist'
    context = {'dok_info': dok_info, 'spcilizname':name}
    return render(request, 'pages/spetializations_doctor.html', context)

    def get_context_data(self, *args, **kwargs):
        context = super(Consultation , self).get_context_data(*args,**kwargs)
        doctor_id = get_object_or_404(Doctor, id = self.kwargs['pk'])
        context['doctor_id'] = doctor_id


# def addconsultation(request,pk):
#     consult_form = ConsaltationsForm
#     if request.method == 'POST' :
#         consult_form = ConsaltationsForm(request.POST)
#         if consult_form.is_valid():
#             consult_form.save()
#     context = {'ConsaltationsForm' : ConsaltationsForm, 'doctor_id' : pk}
#     return render(request, 'pages/addconsultation.html', context)



class AddConsultation(CreateView):
    model = Consaltations
    form_class = ConsaltationsForm 
    template_name = 'pages/addconsultation.html'
    #fields = '__all__'
    # success_url = reverse_lazy('sucess')

    # def form_valid(self, form):
    #     doctor_pk = Doctor.objects.get(pk=self.kwargs['pk'])
    #     category_pk = Doctor.objects.get(spcialty=self.kwargs['c_pk'])
    #     self.object = form.save(commit=False)
    #     self.object.doctor = doctor_pk
    #     self.object.category = category_pk
    #     # self.object.save()
    #     context = {'pk':self.kwargs['pk'],'c_pk':self.kwargs['c_pk']}
    #     return super(AddConsultation, self).form_valid(form)
        
    def get_context_data(self, **kwargs):
        doctor = get_object_or_404(Doctor, id= self.kwargs['pk'])
        context = super(AddConsultation, self).get_context_data(**kwargs)
        context['pk'] = doctor.pk
        context['c_pk'] = doctor.spcialty.pk
        return context


def sucess(request):
    context = {'x':'Your oberation done successfuly'}
    return render(request,'pages/success.html', context)
    