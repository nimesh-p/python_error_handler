import logging
import traceback
from functools import wraps
from rest_framework.exceptions import APIException
from collections import OrderedDict
from rest_framework import status
from django.http import JsonResponse


logger = logging.getLogger(__name__)

class ResponseHandler:
    """ Common Http response handler methods """
    @staticmethod
    def exception_response(
            message="",
            details="",
            status_code: int = status.HTTP_400_BAD_REQUEST,
            *args,
            **kwargs
    ) -> JsonResponse:
        response_dict = OrderedDict(
            message=message,
            status_code=status_code,
            status=False,
            details=details,
        )
        response_dict.update(kwargs)
        return JsonResponse(response_dict, status=status_code)


def error_handler_decorator(
        message=None,
        exception_method=ResponseHandler.exception_response,
        exception_classes=(APIException, ),
        raise_exception=True,
        *args, **kwargs):
    """ Handle the exception on the higher level """
    def decorator(func):
        """ Accept the function wrap it """
        @wraps(func)
        def wrapper(*args, **kwargs):
            """ Wrapper of the actual function """
            try:
                logger.debug(f"{func.__qualname__} method start")
                result = func(*args, **kwargs)
                logger.debug(f"{func.__qualname__} method end")
                return result
            except exception_classes as api_exception:
                # if raise_exception true it will raise exception otherwise return the value
                logger.error(f"{func.__qualname__} {api_exception}")
                if raise_exception:
                    raise api_exception
                return exception_method(message=message)
            except Exception as exc:
                logger.error(f"{func.__qualname__} {exc}", exc_info=True)
                traceback_info = traceback.format_exc()
                return exception_method(message=message, details={'error': str(exc), 'trace_log': traceback_info})
        return wrapper

    return decorator