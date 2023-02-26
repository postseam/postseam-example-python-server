import logging

import grpc
from sqlalchemy import select
from sqlalchemy.orm import Session

from pb.postseam.example.v1.store_pb2 import Store
from pb.postseam.example.v1.store_service_pb2 import CreateStoreRequest
from pb.postseam.example.v1.store_service_pb2 import GetStoreRequest
from pb.postseam.example.v1.store_service_pb2_grpc import StoreServiceServicer
from server.db.store_model import StoreModel
from server.db.util import get_engine
from server.util.helper import validate_firebase


logger = logging.getLogger(__name__)


class StoreService(StoreServiceServicer):
    def CreateStore(
        self, request: CreateStoreRequest, context: grpc.ServicerContext
    ) -> Store:

        if validate_firebase(context) is None:
            logger.warn("Firebase token not verified.")
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("Firebase token not verified.")
            return Store()

        logger.info("Request for CreateStore")
        engine = get_engine()
        with Session(engine) as session:
            # creating the store model
            store_model = StoreModel(
                id=request.id,
                email=request.email,
                business_name=request.business_name,
            )
            # commit to the DB
            session.add(store_model)
            session.commit()

        logger.info("New store inserted in DB")

        # get the string from the incoming request
        store = Store(
            id=request.id, email=request.email, business_name=request.business_name,
        )

        return store

    def GetStore(
        self, request: GetStoreRequest, context: grpc.ServicerContext
    ) -> Store:
        if validate_firebase(context) is None:
            logger.warn("Firebase token not verified.")
            context.set_code(grpc.StatusCode.FAILED_PRECONDITION)
            context.set_details("Firebase token not verified.")
            return Store()

        logger.info("Request for GerStore")
        engine = get_engine()
        with Session(engine) as session:
            store_model = (
                session.query(StoreModel)
                .where(StoreModel.id == request.store_id)
                .first()
            )

        logger.info("Store found in the DB")
        store = Store(
            id=store_model.id,
            email=store_model.email,
            business_name=store_model.business_name,
        )

        return store
