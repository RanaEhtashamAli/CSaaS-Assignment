from django.urls import include, path

urlpatterns = [
    path('api/v1/', include('project.exchangerate.api.v1.urls')),
]
