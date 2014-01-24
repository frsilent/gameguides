from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.models import Account

def accounts(request):
    return render_to_response(
        'accounts/index.html',
        locals(),
        context_instance=RequestContext(request)
    )