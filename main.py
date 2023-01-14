from pb.example.v1.services.store_pb2 import CreateStoreRequest
from pb.example.v1.services.store_pb2 import CreateStoreResponse

from pb.example.v1.services import store_pb2_grpc
from server.services.store import StoreService

import grpc
from concurrent import futures

import logging

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] %(name)-12s [%(levelname)s] %(message)s"
)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=3))

    store_pb2_grpc.add_StoreServiceServicer_to_server(StoreService(), server)

    server.add_insecure_port('0.0.0.0:8000')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
