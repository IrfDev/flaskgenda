from functools import wraps
from flask import request
from datetime import datetime, timedelta
from ...config import Config
from .. import models, api
from ...utils import db
from . import auth
from werkzeug.security import check_password_hash, generate_password_hash
import jwt


def token_required(func):
    """Middleware to authorize users"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_headers = request.headers.get("Authorization")

        if not auth_headers or not auth_headers.startswith("Bearer "):
            return {"detail": 'Missing "Authorization" header'}, 401

        # Getting token based on the value after the prefix

        token = auth_headers.split(" ")[1]

        if not token:
            return {"detail": "Missing token"}, 401

        # Getting token based on the value after the prefix

        try:
            payload = jwt.decode(
                token, Config.SECRET_KEY, algorithms=[Config.JWT_ALGORITHM]
            )
        except jwt.exceptions.ExpiredSignatureError:
            return {"detail": "Token expired"}, 401
        except jwt.exceptions.InvalidTokenError:
            return {"detail": "Invalid token"}, 401

        request.user = db.session.execute(
            db.select(models.User).where(models.User.id == payload["sub"])
        ).scalar_one()

        return func(*args, **kwargs)

    return wrapper


def login():
    try:
        data = request.get_json()
    except:
        pass

    email = data["email"]
    password = data["password"]

    if not all(email, password):
        return {"detail": "missing email or password"}, 400

    # Db operation

    user = db.session.execute(
        db.select(models.User).where(models.User.email == email)
    ).scalar_one_or_none()

    if not all(user, check_password_hash(user.password, password)):
        return {"detail": "invalid email or password"}, 401

    token = jwt.encode(
        {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        Config.SECRET_KEY,
    )

    return {"token": token}


@api.route("/signup/", methods=["POST"])
def signup():
    try:
        data = request.get_json()
    except:
        pass
    email = data["email"]
    password = data["password"]

    if not email:
        return {"detail": "email is required"}, 400

    user_exists = db.session.execute(
        db.select(models.User).where(models.User.email == email)
    ).scalar_one_or_none()

    if user_exists:
        return {"detail": "email already taken"}, 400

    user = models.User(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=email,
        # Required to save the passwords
        password=generate_password_hash(password),
    )
    db.session.add(user)
    db.session.commit()
    return {"detail": "user created successfully"}, 201


@api.route("/login/", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not all(email, password):
        return {"detail": "missing email or password"}, 400

    # Db operation

    user = db.session.execute(
        db.select(models.User).where(models.User.email == email)
    ).scalar_one_or_none()

    if not all(user, check_password_hash(user.password, password)):
        return {"detail": "invalid email or password"}, 401

    token = jwt.encode(
        {
            "sub": user.id,
            "exp": datetime.utcnow() + timedelta(minutes=30),
        },
        Config.SECRET_KEY,
    )

    return {"token": token}
