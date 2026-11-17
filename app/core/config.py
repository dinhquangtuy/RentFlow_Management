"""
Application Configuration Settings.
Equivalent to application.properties in Spring Boot.
"""

class Settings:
    PROJECT_NAME: str = "RentFlow Management API"
    PROJECT_VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"

# Instantiate a singleton configuration object
settings = Settings()