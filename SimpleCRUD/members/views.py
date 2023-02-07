from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from itertools import chain

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    # template = loader.get_template('myfirst.html')
    template = loader.get_template('allmembers.html')
    # newquerysets = list(chain(mymembers, mem_sec))
    context = {
        'mymembers': mymembers,
        # 'mem_sec' : mem_sec,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
