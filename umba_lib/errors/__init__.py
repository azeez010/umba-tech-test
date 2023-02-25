from http import HTTPStatus

from flask import jsonify


class ErrorUtils:
    @staticmethod
    def check_errors(errors):
        if errors:
            return jsonify(errors), HTTPStatus.BAD_REQUEST
