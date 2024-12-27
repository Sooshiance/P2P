import logging
from ipaddress import ip_address

from django.utils.deprecation import MiddlewareMixin

from rest_framework.request import Request
from rest_framework.exceptions import ValidationError


logger = logging.getLogger(__name__)

logging.basicConfig("IP.log", level=logging.WARNING)


class ExtractIPMiddleware(MiddlewareMixin):
    """

    1. Be cautious of trusting the HTTP_X_FORWARDED_FOR header directly, as it can be spoofed.
    This header is typically used when your Django application is behind a proxy or load balancer that
    forwards the original client IP. Ensure your infrastructure is configured correctly to manage trusted proxies.

    2. Rate Limiting: Consider implementing rate limiting or additional checks to prevent abuse from malicious users.

    3. Validation: Ensure that any data coming from users (like ports) is validated and sanitized.

    4. Logging: It might be useful to log any suspicious activities or invalid IP addresses for further analysis.

    """

    def process_request(self, request: Request):
        # Get the client's IP address
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")

        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")

        # Validate the IP address
        try:
            logger.debug("Check the db for more details", logging.DEBUG)
            ip_address(ip)
        except ValidationError:
            logger.warning("Be careful! No IP found!", logging.WARNING)
            ip = None

        # Attach the IP address to the request object
        request.client_ip = ip
        print(request.client_ip)
