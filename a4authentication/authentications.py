import jwt
import time
from django.conf import settings
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import exceptions
from django.contrib.auth import get_user_model

User = get_user_model()


def generate_jwt(user):
    timestamp = time.time() + 7 * 24 * 60 * 60
    token = jwt.encode(
        {"userid": user.id, "exp": timestamp},
        key=settings.SECRET_KEY,
        algorithm="HS256",
    )
    return token


class JWTAuthentication(BaseAuthentication):
    """
    Authorization: JWT 401f7ac837da42b97f613d789819ff93537bee6a
    """

    keyword = "JWT"
    model = None

    """
    A custom token model may be used, but must have the following properties.

    * key -- The string identifying the token
    * user -- The user to which the token belongs
    """

    def authenticate(self, request):
        auth = get_authorization_header(request).split()

        if not auth or auth[0].lower() != self.keyword.lower().encode():
            return None

        if len(auth) == 1:
            msg = "Invalid token header. No credentials provided."
            raise exceptions.AuthenticationFailed(msg)
        elif len(auth) > 2:
            msg = "Invalid token header. Token string should not contain spaces."
            raise exceptions.AuthenticationFailed(msg)

        try:
            jwt_token = auth[1]
            jwt_payload = jwt.decode(
                jwt_token, key=settings.SECRET_KEY, algorithms="HS256"
            )
            userid = jwt_payload.get("userid")
            try:
                user = User.objects.get(pk=userid)
                return (user, jwt_token)
            except Exception:
                msg = "user error"
                raise exceptions.AuthenticationFailed(msg)
        except UnicodeError:
            msg = "Invalid token header. Token string should not contain invalid characters."
            raise exceptions.AuthenticationFailed(msg)

        except jwt.ExpiredSignatureError:
            msg = "token expired"
            raise exceptions.AuthenticationFailed(msg)
