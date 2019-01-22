from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
import os, re, glob

def showFilesList(request):
    args = {}
    directory = 'files'
    os.chdir(directory)
    args['measurementFiles'] = glob.glob("*.txt")
    os.chdir('..')

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('')

    else:
        form = UploadFileForm()

    args['form'] = form

    return render(request, 'graphsBuilder/homePage.html', args)

def handle_uploaded_file(f):
    with open('files/' + str(f) +'.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
