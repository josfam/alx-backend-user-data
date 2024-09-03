#!/usr/bin/env python3
"""
Route module for the API
"""
import os
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

auth = None  # authorization
auth = os.getenv('AUTH_TYPE')
if auth == 'auth':
    from api.v1.auth.auth import Auth

    auth = Auth()
elif auth == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth

    auth = BasicAuth()
else:
    pass


@app.before_request
def check_authorized():
    """Return a json response if the user needs authorization for this path.
    Return an error message if user is not authorized.
    """
    if not auth:
        return
    excluded_paths = [
        '/api/v1/status/',
        '/api/v1/unauthorized/',
        '/api/v1/forbidden/',
    ]
    requested_path = request.path
    if not auth.require_auth(requested_path, excluded_paths):
        return
    # no authorization header
    if auth.authorization_header(request) is None:
        abort(401)
    # no user
    if auth.current_user(request) is None:
        abort(403)


@app.errorhandler(404)
def not_found(error) -> str:
    """Not found handler"""
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Unauthorized handler"""
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """Forbidden error handler"""
    return jsonify({"error": "Forbidden"}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
