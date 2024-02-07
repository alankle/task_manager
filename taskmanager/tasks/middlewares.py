import time 
import logging
from typing import Any

logger = logging.getLogger(__name__)

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    def __call__(self,request) -> Any:
        start_time = time.time()
        response = self.get_response(request)
        duration = time.time() - start_time
        
        logger.warning(f"Request to {request.path} took {duration:.2f} seconds.")
        
        return response