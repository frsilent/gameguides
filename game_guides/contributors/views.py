from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def contributors(request):
    # top4 = Contributors.object.all()[:10]
    return render_to_response(
        'contributors/index.html',
        locals(),
        context_instance=RequestContext(request)
    )