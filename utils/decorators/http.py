from functools import wraps


def access_control_allow(origin, method=None, header=None):
    def decorator(func):
        def control_allow(response):
            if origin:
                origins = ', '.join(origin) if isinstance(origin, list) else origin
                response['Access-Control-Allow-Origin'] = origins

            if method:
                methods = ', '.join(method) if isinstance(method, list) else method
                response['Access-Control-Allow-Methods'] = methods

            if header:
                headers = ', '.join(header) if isinstance(header, list) else header
                response['Access-Control-Allow-Headers'] = headers

        @wraps(func)
        def inner(request, *args, **kwargs):
            response = func(request, *args, **kwargs)
            control_allow(response)
            return response
        return inner
    return decorator