import jwt
import time
from django.conf import settings


def generate_jwt(user):
    timestamp = time.time() + 7 * 24 * 60 * 60
    token = jwt.encode(
        {"userid": user.id, "exp": timestamp},
        key=settings.SECRET_KEY,
        algorithm="HS256",
    )
    return token
