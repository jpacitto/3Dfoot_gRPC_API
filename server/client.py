import grpc
import dfootgeometry_pb2
import dfootgeometry_pb2_grpc

channel = grpc.insecure_channel('127.0.0.1:50051')

stub = dfootgeometry_pb2_grpc.DfootgeometryStub(channel)

userRequest = dfootgeometry_pb2.ProcessImageRequest(uid="2l34j124lk12j4o2ij", identity=None, images=None)

response = stub.ProcessImage(userRequest)

print(response.response)