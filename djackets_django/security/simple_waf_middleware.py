from django.http import HttpResponseForbidden
import logging
import re

class SimpleWAFMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.blocked_ips = []

    def __call__(self, request):
        logging.info(f'Custom WAF Middleware is processing request: {request.path} [{request.method}]')
        response = self.get_response(request)
        return response

    @staticmethod
    # suspicious headers
    def malicious_agent_check(user_agent):
        mal_agents = ['sqlmap', 'python-requests']
        if any(agent in user_agent for agent in mal_agents):
            logging.info('Malicious user agent!')
            return True
        return False

    @staticmethod
    def sql_keyword_check(request):
        # example keywords of possible sql injection
        sql_keywords = ['drop', 'delete', 'insert']
        if request.method == 'GET':
            if (any(key_word in val.lower() for key_word in sql_keywords for val in request.GET.values()) or
                    any(key_word in request.body.decode('utf-8') for key_word in sql_keywords)):
                logging.info('Possible sql attack!')
                return True
        return False

    @staticmethod
    def xss_keyword_check(request):
        # example keywords of possible xss injection
        sql_keywords = ['<script>']
        if request.method == 'POST':
            if (any(key_word in val.lower() for key_word in sql_keywords for val in request.GET.values()) or
                    any(key_word in request.body.decode('utf-8') for key_word in sql_keywords)):
                logging.info('Possible xss attack!')
                return True
        return False

    @staticmethod
    # suspicious headers
    def path_traversal_check(request):
        if re.search(r'\.\./|\.\.\\', request.path):
            logging.info('Possible path traversal attempt!')
            return True
        return False

    def process_view(self, request, view_func, view_args, view_kwargs):
        # NOTE: HERE IS THE LOGIC WHERE WE COULD IMPLEMENT A LOT OF DIFFERENT RULES AND LOGIC
        # TO DETECT MALICIOUS BEHAVIOUR

        user_ip = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT', '').lower()
        logging.info(f'user_ip: {user_ip}, user_agent: {user_agent}')

        # if already been blocked before
        if user_ip in self.blocked_ips:
            logging.info('blocked '+ user_ip)
            return HttpResponseForbidden("Access denied")

        if (SimpleWAFMiddleware.malicious_agent_check(user_agent) or
            SimpleWAFMiddleware.sql_keyword_check(request) or
            SimpleWAFMiddleware.xss_keyword_check(request) or
            SimpleWAFMiddleware.path_traversal_check(request)):
            self.blocked_ips.append(user_ip)
            return HttpResponseForbidden("Access denied")

        logging.info('valid request no rules were triggered')
        # continue processing the request as usual if no rules are triggered
        return None