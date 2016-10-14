from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def mgs_pull(request, spot_id=644):
    # TODO: this needs to be moved to initialized from db
    api_key = "ea3f05d58353822671488b997d52bed6"
    response = requests.get("http://magicseaweed.com/api/{}/forecast/?spot_id={}".format(api_key, spot_id))
    parsed_response = json.loads(response.content)
    return HttpResponse(str(json.dumps(parsed_response, indent=4, sort_keys=True)))

def test(request):
    return render(request, 'polls/swell.html', {})
