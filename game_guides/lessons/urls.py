from django.conf.urls import patterns, url

urlpatterns = patterns('lessons.views',
    url(r'^$', 'lessons', name='lesson-booking'),
)
