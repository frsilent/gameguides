from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.models import UserProfile

def accounts(request):
    print 'accounts view'
    return render_to_response(
        'account/index.htm',
        locals(),
        context_instance=RequestContext(request)
    )