from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.utils import timezone

from models import Guide, GuideFilter


class GuideDetailView(DetailView):
    model = Guide
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        self.object.hit_count += 1
        self.object.save()
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
    top5 = Guide.objects.all().order_by('hit_count')[:5]
    print top5
    filter = GuideFilter(request.GET, queryset=Guide.objects.all())
    return render_to_response('guides/guide_list.html', locals(), context_instance=RequestContext(request))
