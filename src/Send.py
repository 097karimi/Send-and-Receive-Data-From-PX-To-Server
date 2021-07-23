from pymavlink import mavutil
import time
import websocket,json
import Settings


class Send():
    def __init__(self, drone):
        # Start a connection listening to a UDP port
        self.drone = drone

    def send(self,cmd):
        """arm or disarm according to the given parameter.

        Parameters:
            cmd(Bool): if true -> arm,
                        false -> disarm

        Returns: 
            arm_disarm(cmd): return nothing
        """
        ws_cmd = websocket.WebSocket()
        ws_cmd.connect(Settings.ADDR_CMD)
        while True:
            msg = ws_cmd.recv()
            if msg == 'end':
                print(msg)
                time.sleep(0.5)
                continue
            data = json.loads(msg)
            print('', data)
            try:
                if data['arm_state']:
                    # Arm
                    # master.arducopter_arm() or:
                    self.drone.mav.command_long_send(
                        self.drone.target_system,
                        self.drone.target_component,
                        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                        0,
                        1, 0, 0, 0, 0, 0, 0)
                elif not data['arm_state']:
                    # Disarm
                    # master.arducopter_arm() or:
                    self.drone.mav.command_long_send(
                        self.drone.target_system,
                        self.drone.target_component,
                        mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                        0,
                        0, 0, 0, 0, 0, 0, 0)

            except:
                print('No')

        if (cmd == True):
            # Arm
            # master.arducopter_arm() or:
            self.drone.mav.command_long_send(
                self.drone.target_system,
                self.drone.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                1, 0, 0, 0, 0, 0, 0)
        elif(cmd == False):
            # Disarm
            # master.arducopter_disarm() or:
            self.drone.mav.command_long_send(
                self.drone.target_system,
                self.drone.target_component,
                mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
                0,
                0, 0, 0, 0, 0, 0, 0)