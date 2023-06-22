from flask import Flask, jsonify, make_response, request
from flask_swagger_ui import get_swaggerui_blueprint
from user import get_user, create_user


# Create a Flask application instance
app = Flask(__name__)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "User API"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###

# Route to get an user by id


@app.route('/user/<string:user_id>')
def getUserById(user_id):
    return get_user(user_id)


# Route to create a new user
@app.route('/users', methods=['POST'])
def createUser():
    return create_user(request)


# Error handler for HTTP 404 errors
@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)


@app.route('/')
def homepage():
    return 'This is a Server based on the OpenAPI 3.0 specification. <a href="https://topv2h1fuc.execute-api.us-east-1.amazonaws.com/swagger/">Visit swagger page.</a>'
