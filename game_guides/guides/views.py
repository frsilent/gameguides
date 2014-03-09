from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone

from models import Guide, GuideFilter


class GuideListView(ListView):
    model = Guide

    def get_context_data(self, **kwargs):
        context = super(GuideListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


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

def guide_list(request):
    f = GuideFilter(request.GET, queryset=Guide.objects.all())
    return render_to_response('guides/guide_list.html', {'filter': f})

class TestListView(ListView):
    model = Guide

    def get(self, request, *args, **kwargs):
        f = GuideFilter(self.request.GET, queryset = Guide.objects.all())
        return self.render_to_response(
            'guides/f_list2.html',
            context_instance = RequestContext(request)
            )

    def query_set(self):
        return f

 # def get_queryset(self):
 #        publisher = get_object_or_404(Publisher, name__iexact=self.args[0])
 #        return Book.objects.filter(publisher=publisher)


    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})
