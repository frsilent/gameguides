from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.utils import timezone


# class GuideListView(ListView):                                                    # Class based view for listing
#     model = Guide

#     def get_context_data(self, **kwargs):
#         context = super(GuideListView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context



def guides(request):
    # top4 = Contributors.object.all()[:10]
    return render_to_response(
        'guides/index.html',
        locals(),
        context_instance=RequestContext(request)
    )
