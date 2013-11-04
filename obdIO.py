import serial
import time

class OBDport:

    def __init__ (self, tty="/dev/ttyUSB0", baud=115200, time=1):
        try:
            self.port = serial.Serial(tty, baudrate = baud, timeout = time)
            self.port.write("atz\r")
            self.port.write("atsp0\r")
            time.sleep(0.25)
            self.port.flushInput()
        except:
            print ("Could Not open Serial Port")
            raise

    def getData(self, PID):
        try:
            buffer = ""
            self.port.flushInput()
            self.port.flushOutput()
            self.port.write("01" + PID + "\r")
            time.sleep(0.25)
            while True:
                c = self.port.read()
                if c == "\r":
                    break
                else:
                    buffer = buffer + c
            
            buffer = ""
            while True:
                c = self.port.read()
                if c == "\r":
                    break
                else:
                    buffer = buffer + c
                    
            return int(buffer[4:], base=16)

        except ValueError:
            return -1
        except:
            print ("Some Error Occoured getting data from OBD-II")
            raise

            
    
