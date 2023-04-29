from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .task import create_fibonacci
from .models import Fibonacci

from celery.result import AsyncResult

@csrf_exempt
def fibonacci(request):
    if request.method == 'POST':
        n = request.POST.get("key")
        print(n)
        try:
            n = int(n)
            fibonacci = Fibonacci.objects.filter(n=n).first()
            if fibonacci:
                return JsonResponse({
                    'nth': fibonacci.value,
                    'status': 'success'
                })
            else:
                task = create_fibonacci.delay(n)
                task_id = task.task_id
                return JsonResponse({
                    'status': 'pending',
                    'task_id': task_id
                })
        except ValueError:
            pass
