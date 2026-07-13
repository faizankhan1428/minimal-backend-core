"""
Configuration Module

This module contains configuration settings for the Flask application.
Using a class-based configuration approach allows for easy environment-specific
settings and follows Flask best practices.
"""


class Config:
    """
    Base configuration class.
    
    Contains default configuration settings that apply to all environments.
    Additional environment-specific classes can inherit from this base class.
    """
    
    # Flask built-in configuration
    DEBUG = False
    TESTING = False
    
    # Application-specific settings
    API_VERSION = '1.0.0'
    APP_NAME = 'Minimal Backend Core'
    
    # Infrastructure and assignment tracking
    INFRASTRUCTURE_TRACK = 'Backend AI Engineering'
    ASSIGNMENT_CODE = 'BE-01'


class DevelopmentConfig(Config):
    """
    Development environment configuration.
    
    Inherits from Config and overrides settings specific to development.
    """
    DEBUG = True


class ProductionConfig(Config):
    """
    Production environment configuration.
    
    Inherits from Config and overrides settings specific to production.
    """
    DEBUG = False


class TestingConfig(Config):
    """
    Testing environment configuration.
    
    Inherits from Config and overrides settings specific to testing.
    """
    TESTING = True
    DEBUG = True
