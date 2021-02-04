from django.conf.urls import url, include  # noqa: F403
from example.sample.views import index, index2
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^2$', index2, name='index2'),
    # Example:
    # (r'^django_project/', include('django_project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]
