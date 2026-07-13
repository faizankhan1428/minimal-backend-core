"""
Flask Application Factory Module

This module implements the application factory pattern for creating Flask instances.
Following best practices, the app is not initialized globally but created on demand
to enable easier testing and configuration management.
"""

from flask import Flask, jsonify
from app.config import Config
from app.routes import api_bp


def create_app(config_class=Config):
    """
    Application factory function that creates and configures a Flask instance.
    
    Args:
        config_class: Configuration class to use for app configuration.
                     Defaults to Config from app.config module.
    
    Returns:
        Flask: Configured Flask application instance.
    """
    app = Flask(__name__)
    
    # Load configuration from config class
    app.config.from_object(config_class)
    
    # Register the API blueprint containing all routes
    app.register_blueprint(api_bp)
    
    # Register global error handlers for consistent JSON error responses
    register_error_handlers(app)
    
    return app


def register_error_handlers(app):
    """
    Register global error handlers to return JSON responses instead of HTML.
    
    Args:
        app: Flask application instance.
    """
    
    @app.errorhandler(404)
    def not_found(error):
        """
        Handle 404 Not Found errors.
        
        Args:
            error: The error object from Flask.
        
        Returns:
            JSON response with error details and 404 status code.
        """
        return jsonify({
            'error': 'Not Found',
            'message': 'The requested resource was not found on this server.',
            'status_code': 404
        }), 404
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """
        Handle 500 Internal Server Error errors.
        
        Args:
            error: The error object from Flask.
        
        Returns:
            JSON response with error details and 500 status code.
        """
        return jsonify({
            'error': 'Internal Server Error',
            'message': 'An unexpected error occurred on the server.',
            'status_code': 500
        }), 500
