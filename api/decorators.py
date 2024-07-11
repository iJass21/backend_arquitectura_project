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


import functools
import traceback
from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError as DRFValidationError
from django.core.exceptions import ValidationError as DjangoValidationError, ObjectDoesNotExist
from django.db import IntegrityError, DataError
from django.db.utils import OperationalError

def handle_exceptions(func):
    @functools.wraps(func)
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except DRFValidationError as e:
            print(traceback.format_exc())
            return Response({"detail": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except DjangoValidationError as e:
            print(traceback.format_exc())
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e:
            print(traceback.format_exc())
            return Response({"detail": "Database integrity error: " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist as e:
            print(traceback.format_exc())
            return Response({"detail": "Object not found: " + str(e)}, status=status.HTTP_404_NOT_FOUND)
        except DataError as e:
            print(traceback.format_exc())
            return Response({"detail": "Invalid data: " + str(e)}, status=status.HTTP_400_BAD_REQUEST)
        except OperationalError as e:
            print(traceback.format_exc())
            return Response({"detail": "Operational error: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            print(traceback.format_exc())
            return Response({"detail": "An unexpected error occurred: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return inner_function
