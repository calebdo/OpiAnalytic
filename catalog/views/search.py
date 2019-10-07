from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from catalog import models as cmod 
from account import models as amod 
from django import forms

TYPE_FIELD_CHOICES= [
    ('2', 'All'),
    ('0', 'Non-opioids'),
    ('1', 'Opioids'),
]

GENDER_CHOICES= [
    ('O', 'Any'),
    ('M', 'Male'),
    ('F', 'Female'),
]

@view_function
def process_request(request):
    drugs = cmod.Drug.objects.all()

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = UserForm(request.POST)

        if request.user.is_authenticated == False:
            return HttpResponseRedirect('/account/login')

        # Check if the form is valid:
        if form.is_valid(): #ADD CLEAN METHODS from tutorial
            drug_type = form.cleaned_data.get('drug_type')
            drug_name = form.cleaned_data.get('drug_name')
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            return HttpResponseRedirect('/catalog/results/'+ str(drug_type) + '/' + drug_name + '/')

    # If this is a GET (or any other method) create the default form.
    else: #GET
        form = UserForm()

    return request.dmp.render('search.html', {
        'drugs': drugs,
        'form': form,
    })

class UserForm(forms.Form):
    drug_type = forms.IntegerField(label='Select drug type', widget=forms.Select(choices=TYPE_FIELD_CHOICES))
    drug_name= forms.CharField(label='Drug name', max_length=100, required = False)
    #first_name= forms.CharField(label='Prescriber first name', max_length=100, required = False)
    #last_name= forms.CharField(label='Prescriber last name', max_length=100, required = False)
    #gender= forms.CharField(label='Select gender', widget=forms.Select(choices=GENDER_CHOICES))

    def clean(self):
        return self.cleaned_data