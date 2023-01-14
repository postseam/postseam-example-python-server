import grpc

import logging

# Importing store model used requests.
from pb.postseam.example.v1.store_pb2 import Store

# Import request and response objects
from pb.postseam.example.v1.store_service_pb2 import GetStoreRequest
from pb.postseam.example.v1.store_service_pb2 import CreateStoreRequest

# gRPC store service base class. 
from pb.postseam.example.v1.store_service_pb2_grpc import StoreServiceServicer

logger = logging.getLogger(__name__)


class StoreService(StoreServiceServicer):

    def CreateStore(self, request: CreateStoreRequest, context: grpc.ServicerContext) -> Store:

        logger.info("Request for CreateStore")

        # get the string from the incoming request
        store = Store(
            id = request.id,
            email = request.email,
            business_name = request.business_name,
        )

        # TODO: save the newly created store in the database
        return store

    def GetStore(self, request: GetStoreRequest, context: grpc.ServicerContext) -> Store:
        
        logger.info("Request for GetStore")

        # TODO: fetch the store from the database.
        store = Store(
            id = request.store_id,
            email = "email@email.com",
            business_name = "Test Business",
        )
        
        return store
