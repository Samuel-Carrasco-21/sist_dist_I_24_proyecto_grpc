# Documentar y agregar comentarios al codigo

# Importar las bibliotecas necesarias para enviar el client stub
# Completar
import part_one_pb2 as pb

# Completar las elipsis (...)
solicitud_1 = pb.TaxiSolicitud(
    taxi_id=1024,
    conductor_id='123456',
    pasajero_id=["80902", "80102", "80112" ],  # ['Codigo_UPB', 'Codigo_UPB+10', 'Codigo_UPB+20']
    costo_estimado=20
)

# Imprimir el mensaje de solicitud:
print(f"Formato de solicitud:\n{solicitud_1}")