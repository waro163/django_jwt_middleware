# django_jwt_middleware
this project is for Django

you must configure following configuration in the settings.py, eg.

JWT_SECRET = os.environ.get("JWT_SECRET", 'b7y*ef&2a8j_ki&ms*c_o#!zp$!bgk8c=2f%^q@9y16zntsp=2')

MIDDLEWARE = [
    'django_jwt_middleware.middleware.jwt_middleware.JWTMiddleware',
    ...
]