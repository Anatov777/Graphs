from django.shortcuts import render
import os
import re

def showFilesList(request):
    args = {}
    directory = 'files'
    args['measurementFiles'] = os.listdir(directory)

    # f = open('files/blocks_0.txt', 'r')
    # lines = f.readlines()
    # title = lines[0]
    # lines = lines[1:]
    # measurements = []
    # for i in lines:
    # 	if re.search(r'[0-9]+', i):
    # 		measurements += i.split()
    # f.close()
    # args['measurements'] = measurements

    return render(request, 'graphsBuilder/homePage.html', args)
