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

@calculation_controller.route('/extraction')
def extraction() -> str:
    task = celery.send_task('tasks.extraction', kwargs={})
    response = f"task_id : {task.id}"
    return response

@calculation_controller.route('/long_calc')
def long_calc() -> str:
    task = celery.send_task('tasks.long_calc', kwargs={})
    response = f"task_id : {task.id}"
    #TODO: write task_id into postgrsql and task started
    return response

# TODO: reshape this only for checking of status, maybe create additional check point to initialy ask if process exists
@calculation_controller.route('/check', methods=["POST"])
def check_task() -> str:
    req = request.json
    task_id = req.get('task_id')
    res = celery.AsyncResult(task_id)
    if res.state == states.STARTED:
        return res.state
    if res.state == states.PENDING:
        return 'this should not happen: PENDING - only if you ask for un existing process'
    else:
        return str(res.result)

#TODO: endpoint which will retrive real data and will work only if status=SUCCESS and exists in postgresql