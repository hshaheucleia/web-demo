from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('edu.views',
    url('^$', 'index', name='edu_index'),
    url('^search-results/$', 'get_search_results', name='edu_get_search_results'),
    url('^get-streams-for-inst/$', 'get_streams_for_institute', name='edu_get_streams_for_institute'),
    url('^apply-for-inst/$', 'apply_for_institute', name='edu_apply_for_institute'),
    url('^applications/$','my_applications', name='edu_my_applications'),
    url('^delete-application/$','delete_application', name='edu_delete_application'),
    url('^about-institute/$','get_institute_info', name='edu_get_institute_info'),
)


