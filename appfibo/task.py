
from celery import shared_task
from .models import Fibonacci
import logging

logger = logging.getLogger(__name__)

@shared_task
def create_fibonacci(n):
    logger.info("create_fibonacci task started with n=%s", n)

    if n <= 0:
        return

    if n == 1:
        fibonacci_value = '1'
    else:
        a, b = 0, 1
        for i in range(1, n):
            a, b = b, a + b
        fibonacci_value = str(b)

    logger.info("fibonacci_value=%s", fibonacci_value)

    fibonacci = Fibonacci(n=n, value=fibonacci_value)
    fibonacci.save()

    logger.info("create_fibonacci task completed")
