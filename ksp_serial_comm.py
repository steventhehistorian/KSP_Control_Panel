# This class is intended to work with the KSP control panel package to:
#  - List the available serial ports (i.e. to find an Arduino, etc.
#  - Allows the user to select a port to communicate with.
#  - Provides a method for sending serial communication to the selected serial port.

# The Arduino code is saved in a scratch file at: KSP_telemetry_arduino_code.c


import serial
import serial.tools.list_ports
import time


class ToConnect:

    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.serialcomm = serial.Serial(port, baud)

    def sendmessage(self, metric, tosend):

        buffernum = self.serialcomm.out_waiting
        while buffernum > 0:
            pass
        # self.serialcomm.write((" Longitude: " + "\n" + str(tosend) + "\n").encode())
        self.serialcomm.write((" " + metric + ": " + "\n" + str(tosend) + "\n").encode())
        self.serialcomm.flush()
        return print((" " + metric + ": " + "\n" + str(tosend) + "\n"))


    def ask_for_port():
        """\
        Show a list of ports and ask the user for a choice. To make selection
        easier on systems with long device names, also allow the input of an
        index.
        """
        ports = serial.tools.list_ports.comports()
        serConnStr1 = "serialcomm = serial.Serial('"
        serConnStr2 = 0
        serConnStr3 = "',9600)"
        serialOptions = []
        x = 1

        for port, desc, hwid in sorted(ports):
            print("{}. {}: {}".format(x, port, desc))
            serialOptions.append(port)
            x += 1

        print('\n')

        satisfiedCond = 0

        while satisfiedCond == 0:
            i = input("Enter serial port to connect with or type 'exit' to exit: ").strip()
            if i.lower() == 'exit':
                get_out()
            i = int(i)
            print('\n')
            try:
                index = i - 1
                if not 0 <= i - 1 < len(serialOptions):
                    print('--- Invalid index!\n')
                    continue
                satisfiedCond = 1
            except:
                print('except error')
                break
                pass
        else:
            serConnStr2 = serialOptions[i - 1]
            # connectionString = print("{}{}{}".format(serConnStr1,serConnStr2,serConnStr3))
            connectionString = str("{}{}{}".format(serConnStr1, serConnStr2, serConnStr3))

        return connectionString