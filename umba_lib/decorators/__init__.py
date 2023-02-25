from http import HTTPStatus


class ErrorDecorator:
    @staticmethod
    def capture_errors_and_respond(function):
        def function_to_execute(*args, **kwarg):
            try:
                return function(*args, **kwarg)
            except Exception as exc:
                return {"error": str(exc)}, HTTPStatus.INTERNAL_SERVER_ERROR

        function_to_execute.__name__ = function.__name__
        return function_to_execute
