from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Project
from .serializers import ProjectSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.template import loader

# Create your views here.
#function based api views

@csrf_exempt
@api_view(['GET', ])
def projects_all(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        # user_projects = Project.objects.filter(user_id=1)
        serializer = ProjectSerializer(projects, many=True)
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     # data = JSONParser().parse(request)
    #     # serializer = ProjectSerializer(data = data)
    #     serializer = ProjectSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         # return JsonResponse(serializer.data, status=201)
    #         return Response(serializer.errors, status=status.HTTP_201_CREATED)
    #     # return JsonResponse(serializer.errors, status=400)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def user_projects_all(request, usr_id):
    if request.method == 'GET':
        # projects = Project.objects.all()
        user_projects = Project.objects.filter(user_id=usr_id)
        serializer = ProjectSerializer(user_projects, many=True)
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer.data)

    # elif request.method == 'POST':
    #     # data = JSONParser().parse(request)
    #     # serializer = ProjectSerializer(data = data)
    #     print(request.data['p_id'])
    #     user_projects = Project.objects.filter(p_id=request.data['project_id', ], )
    #     print(user_projects)
    #     serializer = ProjectSerializer(data = request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         # return JsonResponse(serializer.data, status=201)
    #         return Response(serializer.errors, status=status.HTTP_201_CREATED)
    #     # return JsonResponse(serializer.errors, status=400)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def retrieve_project(request, usr_id, project_id, flight_id):
    if request.method == 'GET':
        # projects = Project.objects.all()
        print(type(Project.objects.filter(user_id=usr_id,p_id=project_id, f_id=flight_id)))
        user_projects = Project.objects.filter(user_id=usr_id,p_id=project_id, f_id=flight_id).latest('date')
        serializer = ProjectSerializer(user_projects)
        print(user_projects)
        return Response(serializer.data)


        serializer = ProjectSerializer(user_projects)
        # return JsonResponse(serializer.data, safe = False)
        return Response(serializer)

# def retrieve_project(request, usr_id, project_id, flight_id):
#     if request.method == 'GET':
#         # projects = Project.objects.all()
#         print(type(Project.objects.filter(user_id=usr_id,p_id=project_id, f_id=flight_id)))
#         user_projects = Project.objects.filter(user_id=usr_id,p_id=project_id, f_id=flight_id)
#         serializer = ProjectSerializer(user_projects.first())
#         # return JsonResponse(serializer.data, safe = False)
#         return Response(serializer.data)



@api_view(['POST', ])
def store_project(request):
    if request.method == 'POST':
        # data = JSONParser().parse(request)
        # serializer = ProjectSerializer(data = data)
        serializer = ProjectSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            # return JsonResponse(serializer.data, status=201)
            return Response(serializer.errors, status=status.HTTP_201_CREATED)
        # return JsonResponse(serializer.errors, status=400)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def wmq(request):
    latest_question_list = ["Hello is this wmq?", "wat"]
    template = loader.get_template('wmq/wmq.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))




def wmq_params(request, usr_id, project_id, flight_id):
    latest_question_list = ["Hello is this wmq?", "wat"]
    template = loader.get_template('wmq/wmq.html')
    proj = Project.objects.filter(user_id=usr_id, p_id=project_id, f_id=flight_id).first()
    mesh_id = proj.mesh_id
    im_id = proj.ims_id
    def_id = proj.def_id
    context = {
        'mesh_id': mesh_id,
        'im_id': im_id,
        'def_id': def_id,
    }
    return HttpResponse(template.render(context, request))





def wmq_params2(request, task_id):
    latest_question_list = ["Hello is this wmq?", "wat"]
    template = loader.get_template('wmq/wmq.html')
    proj = Project.objects.filter(task_id=task_id).order_by('-date')[0]
    mesh_id = proj.mesh_id
    im_id = proj.ims_id
    def_id = proj.def_id
    context = {
        'mesh_id': mesh_id,
        'im_id': im_id,
        'def_id': def_id,
    }
    return HttpResponse(template.render(context, request))