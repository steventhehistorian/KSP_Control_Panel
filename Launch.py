# import python_serial_COM_Select as serialControl ## disabled until I get this working
import ksp_serial_comm as serialControl  # this has the hardcoded COM port instead of the user selection.
import ksp_server_connect_script as serverconn
import ksp_server_get_values as getvalue
import subprocess
import serial
import time


# Sets up the KSP connection
serverconn

# Sets up the Arduino connection
arduinoSer = serialControl.ToConnect('COM7', 9600)

# Time (seconds) between when values are requested from the KSP server.
delayTimeBetweenCalls = .2

while True:
    arduinoSer.sendmessage(metric="Longitude", tosend=(getvalue.getvalue()))
    time.sleep(delayTimeBetweenCalls)  # gives the arduino time to react


serialControl.serialcomm.close()
