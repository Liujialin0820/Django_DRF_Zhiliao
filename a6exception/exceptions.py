from rest_framework.views import exception_handler
from rest_framework.response import Response


def my_exception_handler(exc, context):
    print(exc)
    print(context)
    print("----")
    response = exception_handler(exc, context)
    if response is None:
        response = Response({"detail": "ops"}, status=500)
    return response
