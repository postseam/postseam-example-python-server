import unittest
from unittest.mock import MagicMock

import grpc
import mock

from pb.postseam.example.v1.store_pb2 import Store
from pb.postseam.example.v1.store_service_pb2 import CreateStoreRequest
from pb.postseam.example.v1.store_service_pb2 import GetStoreRequest
from server.db.store_model import StoreModel
from server.services.store import StoreService


def get_test_store_model():
    return StoreModel(
        id="test_id", email="email@email.com", business_name="Test Business"
    )


class TestStoreService(unittest.TestCase):
    def setUp(self):
        self.store_service = StoreService()

    def get_mock_session(self, mock_session):
        mock_session.return_value.__enter__.return_value.query.return_value.where.return_value.first.return_value = (
            get_test_store_model()
        )

    def get_mock_firebase(self, mock_firebase):
        mock_firebase.return_value = {}

    @mock.patch("server.services.store.get_engine")
    @mock.patch("server.services.store.validate_firebase")
    def test_CreateStore(self, mock_firebase, mock_engine):
        """ Expect to get Store response object """

        self.get_mock_firebase(mock_firebase)
        # mocking some things
        mock_store_model = get_test_store_model()

        request = CreateStoreRequest(
            id=mock_store_model.id,
            email=mock_store_model.email,
            business_name=mock_store_model.business_name,
        )
        response = self.store_service.CreateStore(request, None)

        self.assertIsInstance(response, Store)

        # Validating response proto fields
        self.assertEqual(response.id, request.id)
        self.assertEqual(response.email, request.email)
        self.assertEqual(response.business_name, request.business_name)

    @mock.patch("server.services.store.get_engine")
    @mock.patch("server.services.store.Session")
    @mock.patch("server.services.store.validate_firebase")
    def test_GetStore(self, mock_firebase, mock_session, mock_engine):
        """ Expect to get Store response object """

        # mocking some things
        self.get_mock_session(mock_session)
        self.get_mock_firebase(mock_firebase)
        mock_store_model = get_test_store_model()

        request = GetStoreRequest(store_id=mock_store_model.id)
        response = self.store_service.GetStore(request, None)

        self.assertIsInstance(response, Store)

        # Validating response proto fields
        self.assertEqual(response.id, mock_store_model.id)
        self.assertEqual(response.email, mock_store_model.email)
        self.assertEqual(response.business_name, mock_store_model.business_name)


if __name__ == "__main__":
    unittest.main()
