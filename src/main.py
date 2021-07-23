# Import common module for MAVLink 2
from pymavlink.dialects.v20 import common as mavlink2
from pymavlink import mavutil
import threading
import Settings
from Receive import Recieve
from Send import Send

# Start a connection listening to a UDP port
drone = mavutil.mavlink_connection(Settings.PX_0)

recv = Recieve()
send = Send()

y = threading.Thread(target=recv.recieve)
y.start()
x = threading.Thread(target=send.send)
x.start()

