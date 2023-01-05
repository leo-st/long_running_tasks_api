from http import HTTPStatus
from flask import Blueprint, request, make_response

from services.calculation_service import long_calculation

calculation_controller = Blueprint('calculation_controller', __name__)

@calculation_controller.route("/v1/greetings", methods=["GET"])
def greetings():
    response = make_response({"message": "hello world!"})

    return response