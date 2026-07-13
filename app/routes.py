"""
Routes Module

This module defines all API endpoints using Flask Blueprints.
Blueprints allow for modular route organization and easier maintenance.
Following best practices, all routes are grouped in a single blueprint.
"""

from flask import Blueprint, jsonify
from app.config import Config


# Create a Blueprint for API routes
# The 'api' prefix will be applied to all routes in this blueprint
api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=['GET'])
def root():
    """
    Root endpoint that returns a professional welcome message.
    
    This endpoint serves as the main entry point for the API and provides
    basic information about the service.
    
    Returns:
        JSON response containing welcome message, API version, and status.
        HTTP 200 OK status code.
    """
    return jsonify({
        'message': 'Welcome to the Minimal Backend Core API',
        'description': 'A production-ready Flask backend implementing the request-response '
                      'abstraction loop for distributed systems.',
        'api_version': Config.API_VERSION,
        'status': 'operational',
        'service': Config.APP_NAME
    }), 200


@api_bp.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint that returns service status details.
    
    This endpoint provides infrastructure and assignment tracking information
    for monitoring and verification purposes.
    
    Returns:
        JSON response containing service status, infrastructure track,
        and assignment details. HTTP 200 OK status code.
    """
    return jsonify({
        'status': 'healthy',
        'service': Config.APP_NAME,
        'infrastructure_track': Config.INFRASTRUCTURE_TRACK,
        'assignment': {
            'code': Config.ASSIGNMENT_CODE,
            'description': 'Week 1, Task BE-01 - Production-ready minimal web server'
        },
        'api_version': Config.API_VERSION,
        'timestamp': 'operational'
    }), 200
