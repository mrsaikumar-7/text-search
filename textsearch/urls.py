# myproject/urls.py
from django.contrib import admin
from django.urls import path, include
from paragraph.urls import urlpatterns as paragraphs_urls

# Define URL patterns for the entire project
urlpatterns = [
    # Admin panel URL
    path('admin/', admin.site.urls),

    # Include authentication app's URLs under the 'api/' prefix
    path('api/', include('authentication.urls')),

    # Include Paragraph app's URLs under the 'data/' prefix
    path('data/', include(paragraphs_urls)),
]
