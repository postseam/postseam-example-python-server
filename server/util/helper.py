import json
import logging
import uuid
from datetime import datetime

from firebase_admin import auth

logger = logging.getLogger(__name__)


def get_timestamp_ms():
    return int(datetime.now().timestamp() * 1000)


def generate_uuid():
    return str(uuid.uuid4())


def validate_firebase(context):

    if context is None or context.invocation_metadata() is None:
        logger.warn("Content is empty.")
        return None

    metadata = dict(context.invocation_metadata())
    token = metadata.get("authorization", None)
    if token is None:
        logger.warn("Auth token is not set.")
        return None

    # Verify the token using the verify_id_token method
    try:
        decoded_token = auth.verify_id_token(token)
        logger.info("Validate Firebase token: ", decoded_token)
        return decoded_token
    except Exception as e:
        logger.error("Token is invalid. Error:", e)
