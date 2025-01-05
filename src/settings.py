from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Project settings
    # --------------------------------------------------------------
        
    PROJECT_NAME: str = "troni-api"
    PROJECT_VERSION: str = "1.0.0"
    PROJECT_DESCRIPTION: str = "Simple API to test OpenTelemetry and Jaeger with FastAPI"
    PROJECT_AUTHOR: str = "Roni Hernandez"
    PROJECT_AUTHOR_IMAGE_URL: str = "https://avatars.githubusercontent.com/u/40522363?s=400&u=6840da2e780e3ecdcca4c143e169da6950f2d9e3&v=4"

    # OpenTelemetry settings
    # --------------------------------------------------------------    
    
    SERVICE_NAME: str = "troni-api"
    COLLECTOR_ENDPOINT: str = "localhost"
    COLLECTOR_PORT: int = 4318
    OS_VERSION: str = "1.0.2"
    CLUSTER: str = "A"
    DATACENTRE: str = "BNE"


settings = Settings()