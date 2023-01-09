import os
from datetime import datetime, timedelta, timezone

from flask import Flask
#from flask_jwt_extended import JWTManager, set_access_cookies, create_access_token, get_jwt, get_jwt_identity
#from flask_cors import CORS

from controllers.calculation_controller import calculation_controller

app = Flask(__name__)

# if no environment variable is set, the development config is loaded by default
app.config.from_object(os.getenv("CONFIG_CLASS", "utils.config.Config"))

# Using an `after_request` callback, we refresh any token that is within 30
# minutes of expiring. Change the timedeltas to match the needs of your application.


app.register_blueprint(calculation_controller)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
