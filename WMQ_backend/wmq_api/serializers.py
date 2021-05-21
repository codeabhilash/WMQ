from rest_framework import serializers
from .models import Project



class ProjectSerializer(serializers.ModelSerializer):
        class Meta:
            model = Project
            fields = ['task_id', 'user_id', 'p_id', 'f_id', 'mesh_id', 'ims_id', 'def_id', 'inspection_url', 'date']
