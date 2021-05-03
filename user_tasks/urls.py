from django.urls import path, include
from rest_framework.routers import DefaultRouter

from user_tasks.views import ProjectViewSet

projectRouter = DefaultRouter()
projectRouter.register(r'', ProjectViewSet)

print(projectRouter.urls)

urlpatterns = [
    path('projects/', include(projectRouter.urls), name='projects'),
]
