# ArduPilot SITL + Gazebo Drone Simulation with 1-DOF Gimbal Control

This repository contains the complete implementation of a drone simulation using **ArduPilot SITL**, **Gazebo**, and **MAVLink**, including a **1-DOF gimbal-mounted camera** controlled via MAVLink commands.

The project is divided into **three parts** as per the assignment requirements.

---

## 📌 Task Overview

You are given a drone model in **SDF format**. The objective is to:

1. Integrate the drone with **ArduPilot SITL + Gazebo**
2. Attach a **1-DOF gimbal with camera**
3. Control the gimbal using **MAVLink commands**

---

## 🧩 Part 1 — ArduPilot SITL + Gazebo Drone Integration

### ✔ Objectives
- Set up ArduPilot SITL
- Load the provided drone SDF model into Gazebo
- Establish **bi-directional communication**:
  - SITL → Gazebo: motor outputs
  - Gazebo → SITL: IMU, GPS, Barometer
- Arm and take off the drone
- Demonstrate stable hover / takeoff / landing

### 🛠 Steps Performed
1. Installed ArduPilot SITL following:
   - https://ardupilot.org/dev/docs/sitl-with-gazebo.html
2. Used **Gazebo Classic (v11)** for simulation
3. Loaded the Crazyflie SDF model into Gazebo
4. Integrated `libArduPilotPlugin.so` into the SDF model
5. Verified sensor feedback and motor joint control
6. Armed the drone and tested basic flight commands

### ✅ Expected Output
- Gazebo simulation shows a drone responding to SITL autopilot commands

---

## 🧩 Part 2 — Attach 1-DOF Gimbal + Camera in Gazebo

### ✔ Objectives
- Add a **1-DOF gimbal joint (pitch)**
- Mount a camera on the gimbal
- Display camera feed in a viewer

### 🛠 Steps Performed
1. Integrated `gimbal_small_1d` model with the drone
2. Attached gimbal base using a **fixed joint**
3. Added a **revolute joint** for 1-DOF pitch control
4. Mounted a camera sensor on the gimbal tilt link
5. Enabled camera visualization inside Gazebo

### 🧠 Design Considerations
- Very low mass and inertia to avoid destabilizing the drone
- Gravity disabled for gimbal links
- Damping added to the gimbal joint

### ✅ Expected Output
- Camera feed visible in Gazebo
- Camera view changes as gimbal rotates

---

## 🧩 Part 3 — Gimbal Control via MAVLink Commands

### ✔ Objectives
- Create MAVLink interface using **pymavlink**
- Send gimbal control commands
- Verify physical gimbal motion

### 🛠 MAVLink Commands Used
- `MAV_CMD_DO_MOUNT_CONFIGURE`
- `MAV_CMD_DO_MOUNT_CONTROL`

### 🛠 Steps Performed
1. Connected to ArduPilot SITL via UDP
2. Configured gimbal mount using MAVLink
3. Sent pitch angle commands incrementally
4. Observed gimbal movement in Gazebo

### ✅ Expected Output
- Gimbal moves accurately when MAVLink commands are sent

---

## 📐 SITL ↔ Gazebo Data Flow

