from django.http import HttpResponseForbidden
import logging
import re

class SimpleWAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = []

    def __call__(self, request):
        logging.info("Custom WAF Middleware is processing request: " + request.path)
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # NOTE: HERE IS THE LOGIC WHERE WE COULD IMPLEMENT A LOT OF DIFFERENT RULES AND LOGIC
        # TO DETECT MALICIOUS BEHAVIOUR

        user_ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        logging.info(f'user_ip: {user_ip}, user_agent: {user_agent} \nrequest.GET: {request.GET}')

        # if already been blocked before
        if user_ip in self.blocked_ips:
            logging.info('blocked '+ user_ip)
            return HttpResponseForbidden("Access denied")

        # example keywords of possible sql injection
        for param in request.GET:
            if param.lower() in ['drop', 'delete', 'insert']:
                self.blocked_ips.append(user_ip)
                return HttpResponseForbidden("Potentially harmful request blocked")

        # suspicious headers
        if 'sqlmap' in user_agent or 'python-requests' in user_agent:
            self.blocked_ips.append(user_ip)
            return HttpResponseForbidden("Access denied")

        # content analysis to detect malicious payloads
        if request.method == 'POST':
            for value in request.POST.values():
                if '<script>' in value:  # Basic XSS check
                    return HttpResponseForbidden("Malicious script detected")

        # prevent directory traversal
        if re.search(r'\.\./|\.\.\\', request.path):
            self.blocked_ips.append(user_ip)
            return HttpResponseForbidden("Directory traversal detected")

        logging.info('valid request no rules were triggered')
        # continue processing the request as usual if no rules are triggered
        return None
