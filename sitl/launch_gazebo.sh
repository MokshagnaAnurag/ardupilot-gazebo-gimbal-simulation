#!/bin/bash

export GAZEBO_MODEL_PATH=$HOME/task_submission/models
export GAZEBO_PLUGIN_PATH=$HOME/ardupilot_gazebo/build

gazebo --verbose $HOME/task_submission/worlds/crazyflie.world
