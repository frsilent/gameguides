from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.detail import DetailView
from django.utils import timezone

from endless_pagination.decorators import page_template

from models import Guide
from categories.models import Category


class GuideDetailView(DetailView):
    model = Guide
    slug_field = 'id'

    def get_context_data(self, **kwargs):
        self.object.hit_count += 1
        self.object.save()
        context = super(GuideDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@page_template('guides/guide_list_page.html')
def guide_list(request, template='guides/guide_list.html', extra_context=None):

    context = {
        'top5': Guide.objects.all().order_by('hit_count')[:5],
        'categories': Category.objects.all(),
    }

    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))
