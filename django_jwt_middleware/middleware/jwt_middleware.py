from django.utils.deprecation import MiddlewareMixin
import logging
from ..utils.decode_jwt import decode_jwt

logger = logging.getLogger(__name__)
# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = 'iso-8859-1'

def get_authorization_header(request):
    """
    Return request's 'Authorization:' header, as a bytestring.

    Hide some test client ickyness where the header can be unicode.
    """
    auth = request.META.get('HTTP_AUTHORIZATION', b'')
    if isinstance(auth, str):
        # Work around django test client oddness
        auth = auth.encode(HTTP_HEADER_ENCODING)
    return auth

class JWTMiddleware(MiddlewareMixin):

    keyword = 'Token'

    def process_request(self, request):
        """
        Simple token based authentication.

        Clients should authenticate by passing the token key in the "Authorization"
        HTTP header, prepended with the string "Token ".  For example:

            Authorization: Token 401f7ac837da42b97f613d789819ff93537bee6a
        """
        auth = get_authorization_header(request).split()
        #
        request.META['REMOTE_USER'] = None
        request.META['jwt_payload'] = None
        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return
        try:
            token = auth[1].decode()
            jwt_payload = decode_jwt(token)
            # jwt_payload["token"] = token.decode('utf-8')
            request.META['REMOTE_USER'] = jwt_payload
            request.META['jwt_payload'] = jwt_payload
        except Exception as ex:
            logger.error(ex)