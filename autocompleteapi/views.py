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

# opening file
file = open(os.getcwd() + "/word_search.tsv", "r")
global data
data = []
for i in file.read().split("\n"):
    ele = i.split('\t')
    if len(ele) == 2:
        data.append((int(ele[1]), ele[0]))

#sorting the data based on their usage
data.sort()
data = [x for _, x in data]

def index(request):
   # getting our template
   template = loader.get_template('index.html')
   return HttpResponse(template.render())

class SearchView(APIView):

    # Function that find match through regular expression matching
    def fuzzyfinder(self, user_input, collection):
        suggestions = []
        pattern = '.*?'.join(user_input)   # Converts 'utk' to 'u.*?t.*?k'
        regex = re.compile(pattern)  # Compiles a regex.
        for item in collection:
            match = regex.search(item)   # Checks if the current item matches the regex.
            if match:
                suggestions.append((len(match.group()), match.start(), item))
        return [x for _, _, x in sorted(suggestions)]

    # perform get request of api
    def get(self, request):
        global data
        renderer_classes = [TemplateHTMLRenderer]
        template_name = 'index.html'
        if 'word' in request.GET:
            result = self.fuzzyfinder(user_input=request.GET['word'],collection=data)

        else:
            result = None
        # repond to get request
        return HttpResponse(json.dumps(result), content_type="application/json")
