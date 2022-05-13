# power_project

Requirements:

This application need pika, numpy matplotlib.
pika is used for rabbit mq server and numpy is used for pv simulation, matplotlib for plotting awesome plots.



Working

This application has two components a) Meter: This component is responsible for putting msgs in broker(Rabbitmq) b) Simulator: This component is responsible for reading msgs from Rabbitmq and make pv simulation using the msg. Then it adds this value with the meter value and output the result in a csv file

Note: Step1  keep Rabbitmq up and running before running meter.py and simulator.py

Application will run in two steps

Go to the meter folder and run meter.py python meter.py

Open another tab and go to the simulator folder and run python simulator.py

result will be stored in pv_result.csv in the simulator folder
