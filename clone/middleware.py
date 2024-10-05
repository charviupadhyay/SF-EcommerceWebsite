# middleware.py

from django.utils import timezone
import logging

logger = logging.getLogger(__name__)

class LogUsernameMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        user = request.user
        if user.is_authenticated:
            logger.info(f"[{timezone.now()}] User '{user.username}' accessed {request.path}")
        else:
            logger.info(f"[{timezone.now()}] Anonymous user accessed {request.path}")
        return response
