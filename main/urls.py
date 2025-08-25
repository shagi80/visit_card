from django.urls import path

from .views import IndexPage, ProjectListView, project_images_list
urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('projects/<str:category>/', ProjectListView.as_view(),
         name='projects-category'),
    path('get_project_images/<int:project_pk>', project_images_list,
         name='projects-images'),
]