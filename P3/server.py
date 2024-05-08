from concurrent.futures import ThreadPoolExecutor
from grpc_reflection.v1alpha import reflection
import grpc
import log
import ... as pb
import ... as rpc


def gen_id():
    # el id_gen es un identificador unico
    # se encuentra en formato hex.
    # puede hacer uso de la biblioteca uuid
    id_gen = ...

    return id_gen


class Viaje(rpc.Viaje_rpcServicer):
    def Start(self, request, context):
        # log la solicitud actual
        log.info('viaje: ', request)

        #generar un nuevo id para el ride
        # obtener este id de la funcion generada anteriormente

        id_viaje = ...
        # obtener el costo estimado del viaje 

        costo_viaje = ...

        # generar la respuesta en base a la estructura indicada 
        # en el .proto file.
        respuesta = pb.StartResponse(...)
        return respuesta


if  __name__ == '__main__':
    import config
    # crear una nueva instancia de un servidor gRPC
    # utilizar un ThreadPoolExecutor para manejar las solicitudes entrantes
    server = grpc.server(...)
    # registrar un servicio gRPC en un servidor gRPC
    rpc.add_Viaje_rpcServicer_to_server(Viaje(), server)
    names = (
        # adicionar el nombre del servicio
        pb.DESCRIPTOR.services_by_name['...'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    addr = f'[::]:{config.port}'
    server.add_insecure_port(addr)
    server.start()

    log.info('El servidor esta listo en el puerto%s', addr)
    server.wait_for_termination()
