from django.shortcuts import render
import os

def showFilesList(request):
    args = {}
    directory = 'files'
    args['measurementFiles'] = os.listdir(directory)

    return render(request, 'graphsBuilder/homePage.html', args)
