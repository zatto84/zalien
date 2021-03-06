from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import portal.views



# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', portal.views.home, name='home'),
#    url(r'^login/', include('login.urls')),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^home/', include('portal.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
]
