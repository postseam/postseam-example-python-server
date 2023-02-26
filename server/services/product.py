import logging

import grpc
from sqlalchemy import select
from sqlalchemy.orm import Session

from pb.postseam.example.v1.product_pb2 import Product
from pb.postseam.example.v1.product_service_pb2 import CreateProductRequest
from pb.postseam.example.v1.product_service_pb2 import GetProductRequest
from pb.postseam.example.v1.product_service_pb2 import ListProductsRequest
from pb.postseam.example.v1.product_service_pb2 import ListProductsResponse
from pb.postseam.example.v1.product_service_pb2_grpc import ProductServiceServicer
from server.db.product_model import ProductModel
from server.db.util import get_engine
from server.util.helper import generate_uuid
from server.util.helper import get_timestamp_ms


logger = logging.getLogger(__name__)

MAX_PAGE_SIZE = 50


class ProductService(ProductServiceServicer):
    def CreateProduct(
        self, request: CreateProductRequest, context: grpc.ServicerContext
    ) -> Product:

        logger.info("Request for CreateProduct")
        product_id = generate_uuid()
        create_time = get_timestamp_ms()
        with Session(get_engine()) as session:
            # creating the product model
            product_model = ProductModel(
                id=product_id,
                store_id=request.store_id,
                product_name=request.product_name,
                product_description=request.product_description,
                create_time=create_time,
            )
            # commit to the DB
            session.add(product_model)
            session.commit()

        logger.info("New product inserted in DB")

        # get the string from the incoming request
        product = Product(
            id=product_id,
            store_id=request.store_id,
            product_name=request.product_name,
            product_description=request.product_description,
            create_time=create_time,
        )

        return product

    def GetProduct(
        self, request: GetProductRequest, context: grpc.ServicerContext
    ) -> Product:

        logger.info("Request for GetProduct")
        with Session(get_engine()) as session:
            product_model = (
                session.query(ProductModel)
                .where(ProductModel.id == request.product_id)
                .first()
            )

        logger.info("Product found in the DB")
        product = Product(
            id=product_model.id,
            store_id=product_model.store_id,
            product_name=product_model.product_name,
            product_description=product_model.product_description,
        )

        return product

    def ListProducts(
        self, request: ListProductsRequest, context: grpc.ServicerContext
    ) -> ListProductsResponse:

        logger.info("Request for ListProducts")
        engine = get_engine()
        with Session(engine) as session:
            filters = [
                ProductModel.store_id == request.store_id,
            ]

            page_size = min(request.page_size, MAX_PAGE_SIZE)
            if request.page_token is not None and len(request.page_token) > 0:
                filters.append(ProductModel.create_time < int(request.page_token))

            product_model_list = (
                session.query(ProductModel)
                .filter(*filters)
                .order_by(ProductModel.create_time.desc())
                .limit(page_size)
            )

        product_list = []
        min_create_time = float("inf")
        for product_model in product_model_list:
            product = Product(
                id=product_model.id,
                store_id=product_model.store_id,
                product_name=product_model.product_name,
                product_description=product_model.product_description,
                create_time=product_model.create_time,
            )

            min_create_time = min(min_create_time, product.create_time)
            product_list.append(product)

        if len(product_list) == page_size:
            return ListProductsResponse(
                products=product_list, next_page_token=str(min_create_time)
            )

        return ListProductsResponse(products=product_list)
