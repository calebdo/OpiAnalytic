from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from account import models as amod 

@view_function
def process_request(request):
    prescribers = cmod.Prescriber.objects.all()

    return request.dmp.render('prescriber.html', {
        'prescribers': prescribers,
    })
