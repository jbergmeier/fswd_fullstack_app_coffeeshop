import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc, update
import json
from flask_cors import CORS

from .database.models import db_drop_and_create_all, setup_db, Drink
from .auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers',
                         'GET, POST, PATCH, DELETE, OPTIONS')
    return response


'''
@TODO DONE uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

# ROUTES
'''
@TODO DONE implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['GET'])
def get_drinks():

    try:
        all_drinks = Drink.query.all()
        drinks = [drink.short() for drink in all_drinks]

        return jsonify({
            "success": True,
            "drinks": drinks
        })
    except:
        abort(422)


'''
@TODO DONE implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail', methods=['GET'])
@requires_auth(permission='get:drinks-detail')
def get_drinks_detail(payload):
    try:
        all_drinks = Drink.query.all()
        drinks = [drink.long() for drink in all_drinks]

        return jsonify({
            "success": True,
            "drinks": drinks
        })
    except:
        abort(422)


'''
@TODO DONE implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks', methods=['POST'])
@requires_auth(permission='post:drinks')
def post_drink(payload):
    try:
        new_drink_request = request.get_json()
        new_drink_title = new_drink_request['title']
        new_drink_recipe = new_drink_request['recipe']
        new_drink = Drink(title=new_drink_title,
                          recipe=json.dumps(new_drink_recipe))
        new_drink.insert()

        drinks = [drink.long()
                  for drink in Drink.query.filter(Drink.id == new_drink.id).all()]

        return jsonify({
            "success": True,
            "drinks": drinks
        })

    except:
        abort(422)


'''
@TODO DONE implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth(permission='patch:drinks')
def patch_drink(payload, id):
    drink = Drink.query.filter(Drink.id == id).first()
    if not drink:
        abort(404)
    try:
        updated_drink_request = request.get_json()

        if 'title' in updated_drink_request:
            drink.title = updated_drink_request['title']

        if 'recipe' in updated_drink_request:
            drink.recipe = updated_drink_request['recipe']

        drink.update()

        drinks = [drink.long()
                  for drink in Drink.query.filter(Drink.id == id).all()]

        # print(drink)
        return jsonify({
            "success": True,
            "drinks": drinks
        })

    except:
        abort(422)


'''
@TODO DONE implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''


@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth(permission='post:drinks')
def delete_drink(payload, id):
    drink = Drink.query.filter(Drink.id == id).first()
    if not drink:
        abort(404)
    try:
        drink.delete()
        return jsonify({
            "success": True,
            "delete": id
        })

    except:
        abort(422)


# Error Handling
'''
Example error handling for unprocessable entity
'''


@app.errorhandler(404)
def notFound(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(405)
def notAllowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": "Method not Allowed"
    }), 405


@app.errorhandler(500)
def serverError(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Internal Server Error"
    }), 500


@app.errorhandler(400)
def badRequest(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "Bad Request"
    }), 400


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized"
    }), 401


@app.errorhandler(403)
def accessForbidden(error):
    return jsonify({
        "success": False,
        "error": 403,
        "message": "Access Denied/Forbidden"
    }), 403


@app.errorhandler(AuthError)
def auth_error(e):
    return jsonify({
        "success": False,
        "error": e.status_code,
        "message": e.error
    }), e.status_code


'''
@TODO DONE implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False,
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO DONE implement error handler for 404
    error handler should conform to general task above
'''


'''
@TODO DONE implement error handler for AuthError
    error handler should conform to general task above
'''
