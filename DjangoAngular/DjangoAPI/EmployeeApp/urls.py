from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

from EmployeeApp import views

urlpatterns=[
    re_path(r'^department/$',views.departmentApi),
    re_path(r'^department/([0-9]+)$',views.departmentApi),

    re_path(r'^employee/$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi),

    re_path(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )