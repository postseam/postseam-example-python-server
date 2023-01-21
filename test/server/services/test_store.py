import unittest
import mock

# Importing store model used requests.
from pb.postseam.example.v1.store_pb2 import Store

# Import request and response objects
from pb.postseam.example.v1.store_service_pb2 import GetStoreRequest
from pb.postseam.example.v1.store_service_pb2 import CreateStoreRequest

# gRPC store service implementation 
from server.services.store import StoreService

# Database imports
from server.db.store_model import StoreModel


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

    @mock.patch("server.services.store.get_engine")
    def test_CreateStore(self, mock_engine):
        """ Expect to get CreateStoreResponse """

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
    def test_GetStore(self, mock_session, mock_engine):
        """ Expect to get CreateStoreResponse """

        # mocking some things
        self.get_mock_session(mock_session)
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
