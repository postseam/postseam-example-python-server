import unittest
from unittest.mock import MagicMock

import grpc
import mock

from pb.postseam.example.v1.product_pb2 import Product
from pb.postseam.example.v1.product_service_pb2 import CreateProductRequest
from pb.postseam.example.v1.product_service_pb2 import GetProductRequest
from pb.postseam.example.v1.product_service_pb2 import ListProductsRequest
from pb.postseam.example.v1.product_service_pb2 import ListProductsResponse
from server.db.product_model import ProductModel
from server.services.product import ProductService
from server.util.helper import get_timestamp_ms


def get_test_product_model():
    return ProductModel(
        id="test_id",
        store_id="store_id",
        product_name="Test Product",
        product_description="The best product ever.",
        create_time=get_timestamp_ms(),
    )


def get_test_product():
    product_model = get_test_product_model()

    return Product(
        id=product_model.id,
        store_id=product_model.store_id,
        product_name=product_model.product_name,
        product_description=product_model.product_description,
        create_time=product_model.create_time,
    )


class TestProductService(unittest.TestCase):
    def setUp(self):
        self.product_service = ProductService()

    def get_mock_session(self, mock_session):
        mock_session.return_value.__enter__.return_value.query.return_value.where.return_value.first.return_value = (
            get_test_product_model()
        )

    def list_mock_session(self, mock_session):
        mock_session.return_value.__enter__.return_value.query.return_value.filter.return_value.order_by.return_value.limit.return_value = [
            get_test_product_model()
        ]

    def update_mock_session(self, mock_session):
        mock_session.return_value.query.return_value.get.return_value = (
            get_test_product_model()
        )

    @mock.patch("server.services.product.get_engine")
    def test_CreateProduct(self, mock_engine):
        """ Expect to get Product response object """

        # mocking some things
        mock_product_model = get_test_product_model()

        request = CreateProductRequest(
            store_id=mock_product_model.store_id,
            product_name=mock_product_model.product_name,
            product_description=mock_product_model.product_name,
        )
        response = self.product_service.CreateProduct(request, None)

        self.assertIsInstance(response, Product)

        # Validating response proto fields
        self.assertEqual(response.store_id, request.store_id)
        self.assertEqual(response.product_name, request.product_name)
        self.assertEqual(response.product_description, request.product_description)

    @mock.patch("server.services.product.get_engine")
    @mock.patch("server.services.product.Session")
    def test_GetProduct(self, mock_session, mock_engine):
        """ Expect to get Product response object """

        # mocking some things
        self.get_mock_session(mock_session)
        mock_product_model = get_test_product_model()

        request = GetProductRequest(product_id=mock_product_model.id)
        response = self.product_service.GetProduct(request, None)

        self.assertIsInstance(response, Product)

        # Validating response proto fields
        self.assertEqual(response.id, mock_product_model.id)
        self.assertEqual(response.store_id, mock_product_model.store_id)
        self.assertEqual(response.product_name, mock_product_model.product_name)
        self.assertEqual(
            response.product_description, mock_product_model.product_description
        )

    @mock.patch("server.services.product.get_engine")
    @mock.patch("server.services.product.Session")
    def test_ListProducts(self, mock_session, mock_engine):
        """ Expect to get a list of products """

        # mocking some things
        self.list_mock_session(mock_session)
        mock_product_model = get_test_product_model()

        request = ListProductsRequest(store_id="test", page_size=50)
        response = self.product_service.ListProducts(request, None)

        self.assertIsInstance(response, ListProductsResponse)

        # Validating response proto fields, only one item
        for product in response.products:
            self.assertEqual(product.id, mock_product_model.id)
            self.assertEqual(product.store_id, mock_product_model.store_id)
            self.assertEqual(product.product_name, mock_product_model.product_name)
            self.assertEqual(
                product.product_description, mock_product_model.product_description
            )


if __name__ == "__main__":
    unittest.main()
