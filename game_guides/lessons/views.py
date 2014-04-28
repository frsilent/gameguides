from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import LessonsForm


def lessons(request):
    if request.method == 'POST':
        form = LessonsForm(data=request.POST)
        if form.is_valid():
            pass
    else:
        form = LessonsForm()

    return render_to_response(
        'lessons/index.html',
        locals(),
        context_instance=RequestContext(request)
    )
