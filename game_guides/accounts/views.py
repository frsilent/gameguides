from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.forms import AccountForm

def accounts(request):
    account = request.user.account
    form = AccountForm(instance=account)

    return render_to_response(
        'accounts/index.html',
        locals(),
        context_instance=RequestContext(request)
    )