from DataFrame import DataFrame
from SerialHandler import SerialHandler
from FormatData import FormatData
from FileHandler import FileHandler
from time import sleep

df = DataFrame()
fh = FileHandler(df)
sh = SerialHandler("/dev/ttyACM0", 115200)
sh.openPort()

try:
    while True:
        data = sh.readData(startChar=b'\x02', endChar=b'\x03')

        FormatData.setData(df, data, fh)
        print(df)
        sleep(.01)

except KeyboardInterrupt:
    sh.closePort()

print("FINE")
