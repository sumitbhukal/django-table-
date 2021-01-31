from django.shortcuts import render
from django.http import HttpResponse
# from .forms import NameForm
from .models import data
# Create your views here.
def index(request):
    name = None
    if request.GET.get('name'):
        name = request.GET.get('name')
        emp_id = request.GET.get('emp_id')
        email = request.GET.get('email')
        query = data.object.create(name=name,emp_id=emp_id,email_id=email)
        query.save()
        
    all_data = data.object.all()
    context = {'all_data':all_data}

    return render(request, 'index.html', context)