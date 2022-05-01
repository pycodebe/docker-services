import faktory

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from framework.settings.common import FAKTORY_URL


def index(request):
    return render(request, 'index.html', context={'text': 'Hello World'})


class TaskView(APIView):

    @staticmethod
    def run_a_task(x:int =0, y:int = 0) -> int:
        if x or y is None:
            return 0
        return Response({'result': x + y}, status=status.HTTP_200_OK)
    
    @staticmethod
    def get(request):
        return Response({'data': 'a basic response'}, status=status.HTTP_200_OK)


    def post(self, request) -> None:
        x: int = self.request.POST.get('x')
        y: int = self.request.POST.get('y')
        
        with faktory.connection(faktory=FAKTORY_URL) as client:
            client.queue(
                task=self.run_a_task.__name__,
                queue='default',
                args=(x, y)
            )
        return Response({'data': 'task sent to Faktory'}, status=status.HTTP_200_OK)