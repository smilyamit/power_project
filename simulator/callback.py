import simulator
import json
from datetime import datetime


def callback_func(ch, method, properties, body):
    """
    trial1 : I have tried using randomly generated power value
    but output of PV is not so convincing
    trial 2: take the timestamp to generate simulated PV value
    and write into a csv file.
    """
    received_msg = json.loads(body)

    #tril1 (took input as randomly genetrated power value to generate simulated PV)
    received_msg_val = received_msg['power_value']
    print("Msg received {}".format(received_msg_val))

    #trial2 (Serialize the timestamp to generate simulated PV)
    received_msg['timestamp'] = datetime.fromtimestamp(received_msg['timestamp'])
    #print("Msg received {}".format(received_msg))

    #time_data = received_msg['timestamp']
    #converting time stamp of minute, sec, microsec into hour
    #time_serialized = time_data.hour + time_data.minute/60 + time_data.second/60/60 

    # Get the simulated PV
    pv_simulated = simulator.simulate(received_msg_val)
    #pv_simulated = simulator.simulate(time_serialized)


    # Format the output
    #print("x={} y={}".format(received_msg_val, pv_simulated))
    print("x={} y={}".format(received_msg, pv_simulated))

    # Write the data into csv file
    with open('pv_results.csv', 'a+') as record_file:
        record_file.write('{},{},{},{}\n'.format(received_msg['timestamp'], received_msg['power_value'],
                                                 pv_simulated, pv_simulated+received_msg['power_value']))

    # Acknowledgement
    ch.basic_ack(delivery_tag=method.delivery_tag)
