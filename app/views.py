from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import clases
from app.serializers import claes, claesde


class clas(APIView):
    def get(self,request,*arge,**kearge):
        user_id=kearge.get("id")
        if user_id:
            ems = clases.objects.get(id=user_id)
            ams = claes(ems).data
            return Response({
                "status":200,
                "mig":"查询单个用户成功",
                "resule":ams
            })
        else:
            ems =clases.objects.all()
            ams = claes(ems,many=True).data
            return Response({
                "status": 200,
                "mig": "查询单个用户成功",
                "resule": ams
            })

class declas(APIView):
    print(3)
    def post(self,request,*args,**kwargs):
        user_id = request.data
        print(1)
        if not isinstance(user_id,dict):
            return Response({
                "status":500,
                "mig": "数据有误",
            })
        print(2)
        user = claesde(data=user_id)
        if user.is_valid():
            usere = user.save()
            return Response({
                "status": 201,
                "msg": "用户创建成功",
                "results": claesde(usere).data
            })
        else:
            return Response({
                "status": 501,
                "msg": "用户创建失败",
                "results": user.errors
            })

