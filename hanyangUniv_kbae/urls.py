"""hanyangUniv_kbae URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from pybo.views import total_view


from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('first.html/', total_view.first, name='first'),
    path('waitaminute.html/', total_view.wait, name='wait'),
    
    path('socket_test.html/', total_view.socket, name='socket'),
    
    path('', total_view.base, name='base'),
    path('photos.html/', total_view.photos, name='photos'),
    path('dashboard.html/', total_view.dashboard, name='dashboard'),
    path('sensor.html/', total_view.sensor, name='sensor'),
    path('issue.html/', total_view.issue, name='issue'),
    path('cctv.html/', total_view.cctv, name='cctv'),
    path('map.html/', total_view.mapping, name='map'),
    path('for_ajax.html/', total_view.ajax_test.as_view(), name='ajax'),
    path('contact.html/', total_view.contact, name='contact'),
    path('form.html/', total_view.form, name='form'),
    path('shop.html/', total_view.shop, name='shop'),
    path('about.html/', total_view.about, name='about'),

    
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('video/', include(('video.urls', 'video'), namespace='video')),

    path('', include('detectme.urls')),
]


# handler400 = 'common.views.bad_request_page'
# handler403 = 'common.views.permission_denied'
# handler404 = 'common.views.page_not_found'
# handler500 = 'common.views.server_error'


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
