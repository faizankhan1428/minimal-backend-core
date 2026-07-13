"""
Application Entry Point

This is the main entry point for running the Flask application.
It uses the application factory pattern to create the app instance
and runs the development server on port 5000.
"""

from app import create_app


# Create the Flask application instance using the factory
app = create_app()


if __name__ == '__main__':
    """
    Run the Flask development server.
    
    The server is configured to:
    - Run on host 0.0.0.0 (accessible from external connections)
    - Listen on port 5000
    - Enable debug mode for development (auto-reload on code changes)
    
    Note: For production deployment, use a WSGI server like Gunicorn or uWSGI
    instead of the built-in Flask development server.
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
