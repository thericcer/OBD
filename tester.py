import obdIO


port = obdIO.OBDport()


rpm=0
rpm = port.getData("0c")

print("should be rpm: " + str(rpm))
