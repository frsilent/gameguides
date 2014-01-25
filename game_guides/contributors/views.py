from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import Contributor

def contributors(request):
    contributors = Contributor.objects.all()
    return render_to_response(
        'contributors/index.html',
        locals(),
        context_instance=RequestContext(request)
    )