from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from account import models as amod 


@view_function
def process_request(request, drug_type:int=2, drug_name:str=''):
    drugs = cmod.Drug.objects.all()
    
    if drug_name != '':
        if drug_type != 2:
            drugs = cmod.Drug.objects.filter(is_opioid=drug_type).filter(name=drug_name)
        else:
            drugs = cmod.Drug.objects.filter(name=drug_name)
    elif drug_type != 2:
        drugs = cmod.Drug.objects.filter(is_opioid=drug_type)
    

    print(drugs)
    numresults = drugs.__len__()

    return request.dmp.render('results.html', {
        'drugs': drugs,
        'numresults': numresults
    })