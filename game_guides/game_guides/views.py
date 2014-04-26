from django.http import HttpResponseRedirect, Http404, HttpRequest, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from guides.models import Guide


def index(request):
    """
    Landing page to show why people should use the site
    """

    user_profile = request.user
    videos = Guide.objects.all()[:6]
    features_list = [
        ("Competitive Community Forum", True, True),
        ("CS:S & CS:GO Players' Bible", True, True),
        ("Pro Players' Configs", True, True),
        ("Tips and Tricks", False, True),
        ("Ask the Pros", True, True),
        ("Prizes & Giveaways", True, True),
        ("User Demo Review By Pro", False, True),
        ("Match & Strat commentaries", False, True),
        ("Aim & Crosshair Placement Guides", False, True),
        ("Request a Pro training video", False, True),
        ("Grenade Guides(smoke/flash)", False, True),

    ]

    return render_to_response(
        'index.html',
        locals(),
        context_instance=RequestContext(request)
    )
