from django.db import models

class Project(models.Model):
        task_id = models.AutoField(primary_key=True)
        user_id = models.IntegerField(default=0)
        p_id = models.IntegerField(default=0)
        f_id = models.IntegerField(default=0)
        mesh_id = models.IntegerField(default=0)
        ims_id = models.IntegerField(default=0)
        def_id = models.IntegerField(default=0)
        inspection_url = models.CharField(max_length=200)
        date = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.inspection_url