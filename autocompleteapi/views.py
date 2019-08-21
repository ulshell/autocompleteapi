import re
import os
import json
from django.shortcuts import render
#importing loading from django template
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Search

file = open(os.getcwd() + "/word_search.tsv", "r")
global data
data = []
for i in file.read().split("\n"):
    ele = i.split('\t')
    if len(ele) == 2:
        data.append((int(ele[1]), ele[0]))
data.sort()

data = [x for _, x in data]

def index(request):
   template = loader.get_template('index.html') # getting our template
   return HttpResponse(template.render())

class SearchView(APIView):


    def fuzzyfinder(self, user_input, collection):
        suggestions = []
        pattern = '.*?'.join(user_input)   # Converts 'djm' to 'd.*?j.*?m'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in collection:
            match = regex.search(item)   # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in sorted(suggestions)]


    def get(self, request):
        global data
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'index.html'
        if 'word' in request.GET:
            result = "</br>".join(self.fuzzyfinder(user_input=request.GET['word'],collection=data))
        else:
            result = None
        return Response(result)
