import grpc
from concurrent import futures
import time

import dfootgeometry_pb2
import dfootgeometry_pb2_grpc
import dfootgeometry

class DfootgeometryServicer(dfootgeometry_pb2_grpc.DfootgeometryServicer):

	def ProcessImage(self, request, context):
		response = dfootgeometry_pb2.ProcessImageResponse()
		response.response = dfootgeometry.ImageProcessor(request.uid, request.identity, request.images)
		return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

dfootgeometry_pb2_grpc.add_DfootgeometryServicer_to_server(DfootgeometryServicer(), server)

print('Started server... Listening on IP: 127.0.0.1, PORT: 50051')
server.add_insecure_port('127.0.0.1:50051')
server.start()

try:
	while True:
		time.sleep(86400)
except KeyboardInterrupt:
	server.stop(0)