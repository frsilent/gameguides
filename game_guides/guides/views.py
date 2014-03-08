from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from models import Guide#, GuideFilter


class GuideListView(ListView):
    model = Guide

    # def get_queryset():
    #     category = GuideFilter(self.args[0])
    #     return

    def get_context_data(self, **kwargs):
        context = super(GuideListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# def product_list(request):
#     f = ProductFilter(request.GET, queryset=Product.objects.all())
#     return render_to_response('my_app/template.html', {'filter': f})

 # def get_queryset(self):
 #        publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
 #        return Book.objects.filter(publisher=publisher)


class GuideDetailView(DetailView):
    model = Guide
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        context = super(GuideDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


# def guides(request):
#     # top5 = Guide.objects.all()[:5]
#     # print top5
#     return render_to_response(
#         'guides/index.html',
#         locals(),
#         context_instance=RequestContext(request)
#     )
