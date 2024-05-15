from multiprocessing import context
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail 
# Create your views here.

from hostal_grievance.froms import StudentForm
from hostal_grievance.models import StudentQuery


class Home(TemplateView): 
    template_name = 'hostal_grievance/form.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudentForm() 
        return context

class Submit(CreateView):
    model = StudentQuery
    fields = '__all__'

        
def data(request):
   #print('hello world')
    if request.method == "POST":
        sq = StudentQuery(firstname = request.POST['firstname'], 
        lastname = request.POST['lastname'], 
        roomno = int(request.POST['roomno']),
        sem = int(request.POST['sem']) , 
        email= request.POST['email'],
        branch = int(request.POST['branch']),
        query = request.POST['query']) 
        print(sq.email) 
        send_mail("Query Form",f"Your Response has been Recorded",settings.EMAIL_HOST_USER , [sq.email])
        print('saved the form successfully')
        sq.save()
        # print(request.POST)
        return redirect('/success')
    return render(request ,'hostal_grievance/form.html',{'form':StudentForm()})



class Thanks(TemplateView):
    template_name = 'hostal_grievance/success.html'