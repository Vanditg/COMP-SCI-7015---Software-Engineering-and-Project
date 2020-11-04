from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import csv
import pandas as pd
import numpy as np
from django.utils.safestring import SafeData, SafeString, mark_safe
from django.contrib.auth.decorators import login_required
from .forms import SignInForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
@login_required(login_url='/signin')
def index(request):
    template = loader.get_template('web_app/index.html')
    title = "Real Time Wine Sensing Tool"
    return HttpResponse(template.render({'title': mark_safe(title)}, request))

@login_required(login_url='/signin')
def outlier(request):
    # TODO use CSV module/'data interpreter' here, when ready.
    csv = pd.read_csv("web_app/data/UCI_WineQuality_FakeOutlier.csv")

    # replacing blank spaces with '_'  
    csv.columns = [column.replace(" ", "_") for column in csv.columns]

    csv = csv.query('is_outlier == True')

    # https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.to_html.html

    # TODO - don't use to_html, loop through dataframe in template to generate bootstrap styled html.
    html = csv.to_html(columns=["type", "density", "batch", "datetime", "is_outlier"], justify="left", col_space=150)

    template = loader.get_template('web_app/outlier.html')

    return HttpResponse(template.render({
        'table': mark_safe(html),
        'title': 'Outliers'
    }, request))

@login_required(login_url='/signin')
def batch_analysis(request):
    template = loader.get_template('web_app/batch.html')
    title = "Batch Analysis"
    return HttpResponse(template.render({'title': mark_safe(title)}, request))

@login_required(login_url='/signin')
def barrel_analysis(request):
    template = loader.get_template('web_app/barrel.html')
    title = "Barrel Analysis"
    return HttpResponse(template.render({'title': mark_safe(title)}, request))

@login_required(login_url='/signin')
def manage_batches(request):
    template = loader.get_template('web_app/managebatch.html')
    title = "Manage Batches"
    return HttpResponse(template.render({'title': mark_safe(title)}, request))

@login_required(login_url='/signin')
def manage_account(request):
    template = loader.get_template('web_app/manageaccount.html')
    title = "Manage Account"
    return HttpResponse(template.render({'title': mark_safe(title)}, request))

def signin(request):
    template = loader.get_template('web_app/signin.html')
    title = "Sign In"
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                # Success
                login(request, user)
                # TODO get 'next' querystring. 
                return redirect('/')
            else:
                # Failure
                form.fields['email'].widget.attrs['class'] = 'form-control is-invalid'
                return HttpResponse(template.render({'title': mark_safe(title), 'form': form, 'message': 'Invalid username or password.'}, request))

    else:
        form = SignInForm()

    return HttpResponse(template.render({'title': mark_safe(title), 'form': form}, request))

    
def signout(request):
    logout(request)
    return redirect('/signin/')

@csrf_exempt
def somedata(request):
    # get this from the database, etc etc
    data = {
        'name': 'test response from ajax request'
    }

    return JsonResponse(data)
