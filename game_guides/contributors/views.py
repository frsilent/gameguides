from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from models import Contributor


class ContributorListView(ListView):
    model = Contributor

    def get_context_data(self, **kwargs):
        context = super(ContributorListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ContributorDetailView(DetailView):
    model = Contributor
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(ContributorDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

# def contributors(request):
#     contributors = Contributor.objects.all()
#     return render_to_response(
#         'contributors/index.html',
#         locals(),
#         context_instance=RequestContext(request)
#     )
