import json
import logging

import firebase_admin
from firebase_admin import auth

from server.util.settings import FIREBASE_PATH

logger = logging.getLogger(__name__)


def get_firebase_app():
    if FIREBASE_PATH is None:
        logger.error("Firebase path is not set!")
        return None

    credentials = firebase_admin.credentials.Certificate(FIREBASE_PATH)
    app = firebase_admin.initialize_app(credentials)

    return app
