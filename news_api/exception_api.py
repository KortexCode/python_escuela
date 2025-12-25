"""
Clases para excepciones personalizadas en la conexión a la API
"""
class NewsAPIError(Exception):
    """Excepción personalizada para errores de News API."""

    pass


class ApiKyeError(NewsAPIError):
    """Excepción personalizada para errores de clave API."""

    pass