from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to view any page except for
    those explicitly excluded.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lista de URLs permitidas sem autenticação
        allowed_urls = [
            'login',
            'register',  # Se você tiver uma página de registro
            'admin:index',  # Permitir acesso ao Django admin
        ]

        # Resolver a URL solicitada
        resolver_match = resolve(request.path_info)
        if resolver_match.url_name not in allowed_urls:
            if not request.user.is_authenticated:
                return redirect(settings.LOGIN_URL)
        
        response = self.get_response(request)
        return response
