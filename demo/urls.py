from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from profiles.forms import SignupFormExtra, UserProfileForm
from userena import views as userena_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),

    # Demo Override the signup form with our own, which includes a
    # first and last name.
    # (r'^accounts/signup/$',
    #  'userena.views.signup',
    #  {'signup_form': SignupFormExtra}),
    
    url(r'^accounts/(?P<username>[\.\w-]+)/edit/$',
       userena_views.profile_edit,
       {'edit_profile_form': UserProfileForm },
       name='userena_profile_edit'),

    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^$', 'profiles.views.promo', name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^edu/', include('edu.urls')),
)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


