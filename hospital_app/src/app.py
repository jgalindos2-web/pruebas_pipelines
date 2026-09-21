import requests

def health_message():
    return {"service": "hospital-app", "status": "UP", "http_library": requests.__version__}
