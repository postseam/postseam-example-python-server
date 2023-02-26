import os
import sys

from dotenv import dotenv_values

ENV_PATH = os.path.join(os.environ.get("ENV_FILE_PATH", "./"), ".env")

config = {
  **os.environ,
  **dotenv_values(ENV_PATH)
}

GCP_PROJECT = config.get("GCP_PROJECT", "")
GCP_SQL_REGION = config.get("GCP_SQL_REGION", "")
GCP_SQL_INSTANCE = config.get("GCP_SQL_INSTANCE", "")
GCP_SQL_DATABASE = config.get("GCP_SQL_DATABASE", "")
GCP_SQL_USER = config.get("GCP_SQL_USER", "")
GCP_SQL_PASSWORD = config.get("GCP_SQL_PASSWORD", "")

# Firebase config
FIREBASE_PATH = config.get("FIREBASE_PATH", None)
