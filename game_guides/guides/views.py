from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils import timezone

# from guides.models import Guide
# from django.views.generic.list import ListView




# class GuideListView(ListView):                                                    # Class based view for listing
#     model = Guide

#     def get_context_data(self, **kwargs):
#         context = super(GuideListView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context



def guides(request):
    # top5 = Guide.objects.all()[:5]
    # print top5
    return render_to_response(
        'guides/index.html',
        locals(),
        context_instance=RequestContext(request)
    )
