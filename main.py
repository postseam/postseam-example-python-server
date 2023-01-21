import logging
from concurrent import futures
import grpc

from pb.postseam.example.v1 import store_service_pb2_grpc

from server.db.store_model import StoreModel
from server.db.util import get_engine
from server.services.store import StoreService

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(name)-12s [%(levelname)s] %(message)s"
)


def validate_tables():
    engine = get_engine()

    # Ensure all tables are created correctly
    StoreModel.__table__.create(bind=engine, checkfirst=True)


def serve():

    validate_tables()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))

    store_service_pb2_grpc.add_StoreServiceServicer_to_server(StoreService(), server)

    server.add_insecure_port("0.0.0.0:8000")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
