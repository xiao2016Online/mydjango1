import requests
from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from xiaopy.models import User
# Create your views here.
from xiaopy.serializers import UserSerializer


@api_view(['POST'])
def hello(request):
    r = requests.get('http://www.baidu.com')
    print(r.content)
    return HttpResponse("Hello world!")


def httpPost(request):
    url = 'https://cbh-mgt-cn-north-3.inspurcloud.cn/login'
    data = {"username": "yunxiazi", "password": "Yunanbao@2017"}
    resp = requests.post(url, json=data, verify=False)
    print(resp.content.decode('utf-8'))
    return HttpResponse('123')


#  http 请求例子
#  自定义header
def httpWithHeader(request):
    url = 'http://service-cloud-dev.inspurcloud.cn/regionsvc-cn-north-3/security/v1/admin/categories?queryData='
    headers = {'Content-Type': 'application/json',
               'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJSS0hRaWhSWnBMWS1iQmlmRHdqSEdwSlJNU2JjTzdPQUZXODUzNUtnNlg4In0.eyJqdGkiOiJjMWJlMTU4ZC03ODE2LTQ2OWYtYmFiMi05ZjQ2MTk3MzMzYTciLCJleHAiOjE2MDE0NjMzODksIm5iZiI6MCwiaWF0IjoxNjAxNDU3OTg5LCJpc3MiOiJodHRwczovL2F1dGgtY2xvdWQtZGV2Lmluc3B1cmNsb3VkLmNuL2F1dGgvcmVhbG1zL3BpY3AiLCJhdWQiOlsiY2xpZW50LWluc3B1cnRlc3QwMSIsImFjY291bnQiXSwic3ViIjoiMWQ0NGJmZGEtOGZkMi00ZTJiLWE5OWMtMjFiZGY2OTBjNzUzIiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiY29uc29sZSIsIm5vbmNlIjoiYzFiMWI4MDYtNWZhNS00ZTQ0LThiMTMtZjMyZmRjOTExYjBjIiwiYXV0aF90aW1lIjoxNjAxNDU3OTc0LCJzZXNzaW9uX3N0YXRlIjoiNjQyOTU1MmYtYzM5YS00ODAwLTg3NDUtMTBiYzBmOTExN2YzIiwiYWNyIjoiMSIsImFsbG93ZWQtb3JpZ2lucyI6WyIqIl0sInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJSRFNfQURNSU4iLCJBQ0NPVU5UX0FETUlOIiwib2ZmbGluZV9hY2Nlc3MiLCJ1bWFfYXV0aG9yaXphdGlvbiJdfSwicmVzb3VyY2VfYWNjZXNzIjp7ImNsaWVudC1pbnNwdXJ0ZXN0MDEiOnsicm9sZXMiOlsiYWRtaW4iXX0sImFjY291bnQiOnsicm9sZXMiOlsibWFuYWdlLWFjY291bnQiLCJtYW5hZ2UtYWNjb3VudC1saW5rcyIsInZpZXctcHJvZmlsZSJdfX0sInNjb3BlIjoib3BlbmlkIGVtYWlsIHByb2ZpbGUiLCJlbWFpbF92ZXJpZmllZCI6ZmFsc2UsInByb2plY3QiOiJpbnNwdXJ0ZXN0MDEiLCJncm91cHMiOlsiL2dyb3VwLWluc3B1cnRlc3QwMSJdLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJpbnNwdXJ0ZXN0MDEiLCJlbWFpbCI6Imluc3B1cnRlc3QwMUBpbnNwdXIuY29tIn0.DZWKj9XkTRHNlt3efyQKp3t3hoMZUUnu5OMvW-Qv111G1gVDA6iUc2gF4_fe_knzttIKLBrcHprwWhcihdZAEkjcGQkj9ea0nws_sIhSqphfxm8YeeP6Th_N8SEaSm3NmTSxi9DtRkrNMG4rZlODFDQPRF5iLn-F93ZwFn2NeP1E1C0xEL5LpQR4h1xtfNEjGJrhNsN0zFbPJJn9r2MsCocAf-pl48_pPUymB9_1KhqN2-Dhus5odIaIK9xrKZB3ogFnhrHpPh7BWkJmd7aP1oiwyBWBI5sbWrOvYYh4eEOYnZjRAI_DEeNIIPiVtNBqowvIYTx5HM90Ah5vsME3Ng'}
    resp = requests.get(url, headers=headers, verify=False)
    print(resp.content.decode('utf-8'))
    return HttpResponse(resp.content)


def listAllUser(request):
    result = User.objects.values()
    number = request.GET.get('number', None)
    if number:
        result = result.filter(id=number)
    print(result.query.__str__())
    return HttpResponse('Hello world!1')



# 列表视图
class UserListView(APIView):
    """
    * 需要 token 认证。
    * 只有 admin 用户才能访问此视图
    """
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAdminUser,)
    # GET 查询请求
    def get(self, request):
        result = User.objects.values()
        json = UserSerializer(result, many=True)
        # return JsonResponse(json.data,safe=False,status=201)
        return Response(json.data)

    # POST 请求
    def post(self, request):
        user = UserSerializer(data=request.data, many=False)
        print(request.data)
        if user.is_valid():
            # print('start== %s' % user)
            user.save()
            return Response(user.data)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


# 详情视图
class UserDetailView(APIView):
    def get(self, request, pk):
        student = User.objects.get(id=pk)
        if not student:
            return Response(None,status=status.HTTP_404_NOT_FOUND)
        print('student %s' % student)
        serializer = UserSerializer(student)
        print(serializer.data)
        return Response(serializer.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.data, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk):
        instance=User.objects.get(pk=pk)
        user = UserSerializer(data=request.data,instance=instance)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        User.objects.get(id=pk).delete()
        return Response()

# 分页类声明
class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

# 自定义分页
class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000
    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #     'next1': self.get_next_link(),
            #     'previous1': self.get_previous_link()
            # },
            'pageSize':self.page.number,
            'count': self.page.paginator.count,
            'data': data
        })


# class
class UserDetail(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination


