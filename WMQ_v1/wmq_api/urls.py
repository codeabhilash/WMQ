from django.urls import path
from .views import projects_all, retrieve_project, store_project, user_projects_all
from . import views

urlpatterns = [
    path('api/project_list/', projects_all),
    path('api/project/', store_project),
    # path('api/projects/user/<int:usr_id>', user_projects_all),
    path('api/project/user/<int:usr_id>/project/<int:project_id>/flight/<int:flight_id>', retrieve_project),
    path('task/<int:task_id>', views.wmq_params2, name='wmq'),
    # path('wmq/user/<int:usr_id>/project/<int:project_id>/flight/<int:flight_id>', views.wmq_params, name='wmq2'),
]
