from sqlalchemy import create_engine
from google.cloud.sql.connector import Connector

from server.util.settings import GCP_PROJECT
from server.util.settings import GCP_SQL_DATABASE
from server.util.settings import GCP_SQL_INSTANCE
from server.util.settings import GCP_SQL_PASSWORD
from server.util.settings import GCP_SQL_REGION
from server.util.settings import GCP_SQL_USER


def get_cloud_sql_connection():
    connector = Connector()

    return connector.connect(
        f"{GCP_PROJECT}:{GCP_SQL_REGION}:{GCP_SQL_INSTANCE}",
        "pg8000",
        user=f"{GCP_SQL_USER}",
        password=f"{GCP_SQL_PASSWORD}",
        db=f"{GCP_SQL_DATABASE}",
    )

def get_engine():
    if GCP_PROJECT == "":
        engine = create_engine(
            "postgresql://user:password@localhost:5432/postseam", echo=True
        )
    else:
        engine = create_engine("postgresql+pg8000://", creator=get_cloud_sql_connection, echo=True,)
        
    return engine
