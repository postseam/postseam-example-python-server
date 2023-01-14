import unittest

# Importing store model used requests.
from pb.postseam.example.v1.store_pb2 import Store

# Import request and response objects
from pb.postseam.example.v1.store_service_pb2 import GetStoreRequest
from pb.postseam.example.v1.store_service_pb2 import CreateStoreRequest

# gRPC store service implementation 
from server.services.store import StoreService


class TestStoreService(unittest.TestCase):
    def setUp(self):
        self.store_service = StoreService()

    def test_CreateStore(self):
        """ Expect to get CreateStoreResponse """
        
        request = CreateStoreRequest(
            id="test_id",
            email="test@test.com",
            business_name="Test Business",
        )

        response = self.store_service.CreateStore(request, None)

        self.assertIsInstance(response, Store)

        # Validating response proto fields 
        self.assertEqual(response.id, request.id)
        self.assertEqual(response.email, request.email)
        self.assertEqual(response.business_name, request.business_name)

    def test_GetStore(self):
        """ Expect to get CreateStoreResponse """
        
        request = GetStoreRequest(
            store_id="test_id",
        )

        response = self.store_service.GetStore(request, None)

        self.assertIsInstance(response, Store)

        # Validating response proto fields 
        self.assertEqual(response.id, request.store_id)
        self.assertEqual(response.email, "email@email.com")
        self.assertEqual(response.business_name, "Test Business")

if __name__ == '__main__':
    unittest.main()
