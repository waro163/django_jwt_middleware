import jwt
from .get_settings_value import get_setting_value

def decode_jwt(token,algorithms='HS256'):
    jwt_secret = get_setting_value('JWT_SECRET')
    try:
        jwt_payload = jwt.decode(token, jwt_secret, algorithms=[algorithms])
    except Exception as e:
        raise e
    return jwt_payload