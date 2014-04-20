from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    user_profile = request.user

    return render_to_response(
        'index.html',
        locals(),
        context_instance=RequestContext(request)
    )
