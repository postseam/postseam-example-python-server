# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pb/postseam/example/v1/product_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pb.postseam.example.v1 import product_pb2 as pb_dot_postseam_dot_example_dot_v1_dot_product__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,pb/postseam/example/v1/product_service.proto\x12\x16pb.postseam.example.v1\x1a$pb/postseam/example/v1/product.proto\"[\n\x14\x43reateProductRequest\x12\x10\n\x08store_id\x18\x01 \x01(\t\x12\x14\n\x0cproduct_name\x18\x02 \x01(\t\x12\x1b\n\x13product_description\x18\x03 \x01(\t\"\'\n\x11GetProductRequest\x12\x12\n\nproduct_id\x18\x01 \x01(\t\"N\n\x13ListProductsRequest\x12\x10\n\x08store_id\x18\x01 \x01(\t\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"b\n\x14ListProductsResponse\x12\x31\n\x08products\x18\x01 \x03(\x0b\x32\x1f.pb.postseam.example.v1.Product\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xbb\x02\n\x0eProductService\x12Z\n\nGetProduct\x12).pb.postseam.example.v1.GetProductRequest\x1a\x1f.pb.postseam.example.v1.Product\"\x00\x12`\n\rCreateProduct\x12,.pb.postseam.example.v1.CreateProductRequest\x1a\x1f.pb.postseam.example.v1.Product\"\x00\x12k\n\x0cListProducts\x12+.pb.postseam.example.v1.ListProductsRequest\x1a,.pb.postseam.example.v1.ListProductsResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'pb.postseam.example.v1.product_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEPRODUCTREQUEST._serialized_start=110
  _CREATEPRODUCTREQUEST._serialized_end=201
  _GETPRODUCTREQUEST._serialized_start=203
  _GETPRODUCTREQUEST._serialized_end=242
  _LISTPRODUCTSREQUEST._serialized_start=244
  _LISTPRODUCTSREQUEST._serialized_end=322
  _LISTPRODUCTSRESPONSE._serialized_start=324
  _LISTPRODUCTSRESPONSE._serialized_end=422
  _PRODUCTSERVICE._serialized_start=425
  _PRODUCTSERVICE._serialized_end=740
# @@protoc_insertion_point(module_scope)