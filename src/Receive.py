import websocket,json
import Settings


class Recieve:
    def __init__(self, drone):
        # Start a connection listening to a UDP port
        self.drone = drone

    def recieve(self):
        """ recieve data from Pixhawk

        Parameters:
            recieve(self): 'self' got passed itself

        Returns: 
            recieve(cmd): send data to given address through websocket
        """
        ws = websocket.WebSocket()
        ws.connect(Settings.ADDR_RECV)

        lat = 0
        lon = 0
        voltage_battery = 0
        current_battery = 0
        roll = 0
        pitch = 0
        yaw = 0
        alt = 0
        airspeed = 0
        velocity_variance = 0
        servo1_raw = 0
        servo2_raw = 0
        servo3_raw = 0
        servo4_raw = 0
        servo5_raw = 0
        servo6_raw = 0
        servo7_raw = 0
        servo8_raw = 0
        vibration_x = 0
        vibration_y = 0
        vibration_z = 0
        
        while True:
            msg = self.drone.recv_match(blocking=True)
            if msg.to_dict()['mavpackettype'] == 'GLOBAL_POSITION_INT':
                lat = msg.lat
                lon = msg.lon
            elif msg.to_dict()['mavpackettype'] == 'SYS_STATUS':
                voltage_battery = msg.voltage_battery
                current_battery = msg.current_battery
            elif msg.to_dict()['mavpackettype'] == 'ATTITUDE':
                roll = msg.roll
                pitch = msg.pitch
                yaw = msg.yaw
            elif msg.to_dict()['mavpackettype'] == 'VFR_HUD':    
                alt = msg.alt
                airspeed = msg.airspeed
            elif msg.to_dict()['mavpackettype'] == 'EKF_STATUS_REPORT':            
                velocity_variance = msg.velocity_variance
            elif msg.to_dict()['mavpackettype'] == 'SERVO_OUTPUT_RAW':
                servo1_raw = msg.servo1_raw
                servo2_raw = msg.servo2_raw
                servo3_raw = msg.servo3_raw
                servo4_raw = msg.servo4_raw
                servo5_raw = msg.servo5_raw
                servo6_raw = msg.servo6_raw
                servo7_raw = msg.servo7_raw
                servo8_raw = msg.servo8_raw
            elif msg.to_dict()['mavpackettype'] == 'VIBRATION':
                vibration_x = msg.vibration_x
                vibration_y = msg.vibration_y
                vibration_z = msg.vibration_z
            
            
            data = {
                "lat" : lat,
                "lng" : lon,
                "voltage_battery" : voltage_battery,
                "current_battery" : current_battery,
                "roll" : roll,
                "pitch" : pitch,
                "yaw" : yaw,
                "alt" : alt,
                "airspeed" : airspeed,
                "velocity_variance" : velocity_variance,
                "servo1_raw" : servo1_raw,
                "servo2_raw" : servo2_raw,
                "servo3_raw" : servo3_raw,
                "servo4_raw" : servo4_raw,
                "servo5_raw" : servo5_raw,
                "servo6_raw" : servo6_raw,
                "servo7_raw" : servo7_raw,
                "servo8_raw" : servo8_raw,
                "vibration_x" : vibration_x,
                "vibration_y" : vibration_y,
                "vibration_z" : vibration_z,
            }
            data_in_json = json.dumps(data)
            ws.send(data_in_json)