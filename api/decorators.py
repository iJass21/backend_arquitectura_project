# api/decorators.py
from functools import wraps
from rest_framework.response import Response
from rest_framework import status

def validate_serializer(serializer_class):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if request.method == 'POST':
                serializer = serializer_class(data=request.data, files=request.FILES)
                if serializer.is_valid():
                    return func(self, request, serializer, *args, **kwargs)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return func(self, request, *args, **kwargs)
        return wrapper
    return decorator
