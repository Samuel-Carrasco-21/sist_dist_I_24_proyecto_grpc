# Completar...
import part_one_pb2 as pb
import json
import pickle

# El resto del codigo aca

with open('sample_request_data.json', 'r') as json_file:
    sample_request_data = json.load(json_file)

# print(sample_request_data)

taxi_id = sample_request_data['taxi_id']
conductor_id = sample_request_data['conductor_id']
pasajero_id = sample_request_data['pasajero_id']
costo_estimado = sample_request_data['costo_estimado']
result = []
for key in range(0,100):
    result.append({
        "taxi_id": taxi_id[f'{key}'],
        "conductor_id": conductor_id[f'{key}'],
        "pasajero_id": pasajero_id[f'{key}'].split(','),
        "costo_estimado": costo_estimado[f'{key}']
    })

print(result)

def marshallazingInputs(list_gotten):
    messages_list = []
    for message in list_gotten:
        messageResult = pb.TaxiSolicitud(
            taxi_id= message['taxi_id'],
            conductor_id= message['conductor_id'],
            pasajero_id= message['pasajero_id'],
            costo_estimado= message['costo_estimado']
        )
        messages_list.append(messageResult.SerializeToString())

    return messages_list


marshall_sample_request_data = marshallazingInputs(result)

def printList(itemList):
    for item in itemList:
        print(item)

printList(marshall_sample_request_data)

sample_request_data_bin = 'output_p1b.bin'

# generate bin:
with open(sample_request_data_bin, 'wb') as file:
    pickle.dump(marshall_sample_request_data, file)
print(f'marshall_sample_request_data saved at {sample_request_data_bin}.bin')
