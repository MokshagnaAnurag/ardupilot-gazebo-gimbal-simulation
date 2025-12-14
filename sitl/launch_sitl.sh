#!/bin/bash

cd ~/ardupilot/build/sitl/bin

./arducopter \
  --model gazebo \
  --speedup 1 \
  --defaults=$HOME/task_submission/sitl/crazyflie.parm

