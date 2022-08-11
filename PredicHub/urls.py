from django.contrib import admin
from django.urls import path, include
from .views import index

# Media Url
from .settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),

    # Include Apps
    path("admission/", include("admission.urls")),
    path("job/", include("job.urls")),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)
