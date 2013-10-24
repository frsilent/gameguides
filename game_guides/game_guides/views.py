from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def home(request):
    # user_profile = request.user.get_profile()
    # print user_profile

    return render_to_response(
        'base.html',
        locals(),
        context_instance=RequestContext(request)
    )
