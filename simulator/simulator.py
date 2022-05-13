
import math
import pika
import numpy as np
import callback

'''formula for normal distribution is given by :
   1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
   
   let say mean = 0 then std = 1
'''
#def simulate(time_serialized):
def simulate(x):
    """
    Simulator function to make PV simulator
    """
    # pv simulation using numpy expression
    mean = 0
    variance = 1
    std = math.sqrt(variance)
    y_out =  np.exp( x - mean)**2 /(2* std**2)
    #y_out = 1/(std * np.sqrt(2 * np.pi)) * np.exp( - (x - mean)**2 / (2 * std**2))
    return y_out


def start_receive_msg():
    """
    This method will consume the msgs from the rabbitmq
    """
    #connection establishment
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # queue declaration
    channel.queue_declare(queue='meter', durable=True)
    channel.basic_consume(queue='meter', on_message_callback=callback.callback_func)
    print('All messages are consumed.. Waiting for new messages')
    channel.start_consuming()


if __name__ == '__main__':
    # Start receiving msg from Rabbit MQ
    start_receive_msg()

