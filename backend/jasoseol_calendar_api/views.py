from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from mongoengine import Q

from .models import Todo
from .Serializers import TodoSerializer

from datetime import datetime
from dateutil.relativedelta import *


# Create your views here.
class TodoView(APIView):
    def get(self, request):
        serializer = TodoSerializer(Todo.objects.all(), many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class TodoMonthView(APIView):
    def get(self, request, year, month):
        serializer = TodoSerializer(Todo.objects.all(), many=True)
        data = serializer.data

        response_data = []
        start_date = datetime.strptime(str(year) + '-' + str(month), "%Y-%m") + relativedelta(months=-1)
        end_date = datetime.strptime(str(year) + '-' + str(month), "%Y-%m") + relativedelta(months=+2, days=-1)

        for d in data:
            target_date = datetime.strptime(d['date'], '%Y-%m-%d')

            if start_date < target_date < end_date:
                response_data.append(d)

        return Response(response_data, status=status.HTTP_200_OK)


class TodoDateView(APIView):
    def get(self, request, year, month, date):
        response_data = {}
        try:
            todo_object = Todo.objects.get(date="{}-{}-{}".format(year, month, date))
            if todo_object:
                response_data = TodoSerializer(todo_object).data
        except:
            pass

        return Response(response_data, status=status.HTTP_200_OK)

    def post(self, request, year, month, date):
        response_data = {}

        try:
            req_data = request.data
            req_data['date'] = "{}-{}-{}".format(year, month, date)

            todo = Todo()
            todo.date = datetime.strptime(req_data['date'], "%Y-%m-%d")
            todo.event = request.data['event']
            todo.save()

            response_data = TodoSerializer(request.data).data
        except:
            pass

        return Response(response_data, status=status.HTTP_200_OK)
