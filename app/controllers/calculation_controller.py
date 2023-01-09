from http import HTTPStatus
from flask import Blueprint, request, make_response
from worker import celery
import celery.states as states


from services.calculation_service import long_calculation

calculation_controller = Blueprint('calculation_controller', __name__)

@calculation_controller.route("/v1/greetings", methods=["GET"])
def greetings():
    response = make_response({"message": "hello world!"})

    return response

@calculation_controller.route('/extraction/')
def extraction() -> str:
    task = celery.send_task('tasks.extraction', kwargs={})
    response = f"task_id : {task.id}"
    return response

@calculation_controller.route('/check', methods=["POST"])
def check_task() -> str:
    req = request.json
    task_id = req.get('task_id')
    res = celery.AsyncResult(task_id)
    if res.state == states.PENDING:
        return res.state
    else:
        return str(res.result)