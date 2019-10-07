from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
from django import forms


#convert to our use
@view_function
def process_request(request):
   

    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = MyForm(request.POST)

        # Check if the form is valid:
        if form.is_valid(): #ADD CLEAN METHODS from tutorial
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')

    # If this is a GET (or any other method) create the default form.
    else: #GET
        form = MyForm()

    context = {

        'form': form,
    }

    return request.dmp.render('login.html', context)

class MyForm(forms.Form): # not totally sure if this is right
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data