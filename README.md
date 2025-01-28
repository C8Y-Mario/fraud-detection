# Fraud Detection 

## Overview

This project translates the Hazelcast Fraud Detection Example from https://github.com/hazelcast/fraud-detection-onnx to
Apama and Python. Example data and model are taken from the Github project.

### Input 
The project reads transaction data from a CSV and publishes them as JSON on MQTT
Apama will read in the transaction data from the MQTT broker. The context data (customers, merchants) are read directly 
from CSV files.

### Output
The project runs an inference on each transaction and will output the CreditCard number for each potential fraud.

## Setup 

### ONNX plugin
**Before running this project you must install ONNX Engine**
- Open an Apama Command Prompt
- run : pip install numpy onnxruntime

### MQTT
install a local broker (e.g. mosquitto)

### Jmeter 
- Install Jmeter
- Install Jmeter MQTT plugin:
  - download jar from https://github.com/emqx/mqtt-jmeter/releases
  - put jar into apache-jmeter-<version>\lib\ext
- Load jmx file
  - Make sure broker port matches your installation
  - Adjust the path in the "CSV Data Set Config" step to the transaction file

## Run
- Run Apama project
- Run JMeter script