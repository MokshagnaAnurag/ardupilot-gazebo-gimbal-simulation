#!/usr/bin/env python3
from pymavlink import mavutil
import time
import math

# Connect to SITL
master = mavutil.mavlink_connection('udp:127.0.0.1:14550')

print("Waiting for heartbeat...")
master.wait_heartbeat()
print("Connected to system %d component %d" %
      (master.target_system, master.target_component))

# --------------------------------------------------
# Configure gimbal for MAVLink control
# --------------------------------------------------
print("Configuring gimbal...")

master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_DO_MOUNT_CONFIGURE,
    0,   # confirmation
    mavutil.mavlink.MAV_MOUNT_MODE_MAVLINK_TARGETING,  # param1
    0,   # param2 stabilize roll
    0,   # param3 stabilize pitch
    0,   # param4 stabilize yaw
    0,   # param5
    0,   # param6
    0    # param7   REQUIRED
)

time.sleep(1)

# --------------------------------------------------
# Move gimbal (PITCH only – 1 DOF)
# --------------------------------------------------
print("Moving gimbal...")

for pitch_deg in range(0, -45, -5):
    pitch_rad = math.radians(pitch_deg)

    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_DO_MOUNT_CONTROL,
        0,              # confirmation
        pitch_rad,      # param1: pitch (radians)
        0,              # param2: roll
        0,              # param3: yaw
        0,              # param4
        0,              # param5
        0,              # param6
        0               # param7 REQUIRED
    )

    print(f"Gimbal pitch: {pitch_deg} degrees")
    time.sleep(0.7)

print("Gimbal test complete.")
