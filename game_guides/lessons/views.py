from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def lessons(request):
    return render_to_response(
        'lessons/index.html',
        locals(),
        context_instance=RequestContext(request)
    )