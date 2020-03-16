import csv, time
from GUI.RealTime import DataFrame

class FileHandler:

    __doc__='''Documentation for FormatData.py functions:

    __init__(self, dataFrame):
        creates a fileHandler object to save data in a CSV file called "dd_mm_yyyy  hh_mm__ss.csv"
        the fileHandler object has a dataFrame variable where the dataFrame is saved
        it opens the three files in order to have them ready to be written

    write100Hz():
        writes new 100Hz data inside the .csv file.
        In order to save data carefully it closes the file every 500 writings (5 seconds)

    write10Hz():
        writes new 10Hz data inside the .csv file.
        In order to save data carefully it closes the file every 50 writings (5 seconds)

    write4Hz():
        writes new 4Hz data inside the .csv file.
        In order to save data carefully it closes the file every 20 writings (5 seconds)
    '''

#Creates a FileHandler object to save data in a CSV file called "dd_mm_yyyy  hh_mm__ss.csv"

    def __init__(self, dataFrame):
        self.__dataFrame = dataFrame
        nome = time.strftime("%a_%d_%b_%Y") + " " + time.strftime("%H_%M_%S_")
        self.__name100Hz = nome + "100Hz.csv"
        self.__name10Hz = nome + "10Hz.csv"
        self.__name4Hz = nome + "4Hz.csv"
        self.__fieldnames100Hz  = ['rpm', 'tps', 'accel_x', 'accel_y', 'accel_z', 'gyro_x', 'gyro_y', 'gyro_z', 'pot_fsx',  'pot_fdx', 'pot_FAccuracy', 'pot_rsx',  'pot_rdx', 'pot_RAccuracy','steeringEncoder']
        self.__fieldnames10Hz  = ['t_h20', 't_air', 't_oil', 'vbb', 'lambda1_avg', 'lambda1_raw', 'k_lambda1', 'inj_low', 'inj_high']
        self.__fieldnames4Hz = [''] #DA FARE
        self.__lineNumber100Hz = 0
        self.__lineNumber10Hz = 0
        self.__lineNumber4Hz = 0

        self.__file100Hz = open(self.__name100Hz, 'w', newline='')
        self.__writerFile100Hz = csv.writer(self.__file100Hz, delimiter=';', dialect='excel')
        self.__writerFile100Hz.writerow(self.__fieldnames100Hz)
        
        self.__file10Hz = open(self.__name10Hz, 'w', newline='')
        self.__writerFile10Hz = csv.writer(self.__file10Hz, delimiter=';', dialect='excel')
        self.__writerFile10Hz.writerow(self.__fieldnames10Hz)
        
        # 4Hz ANCORA NON IN USO
        # self.__file4Hz = open(self.__name4Hz, 'w', newline='')
        # self.__writerFile4Hz = csv.writer(self.__file4Hz, delimiter=';', dialect='excel')
        # self.__writerFile4Hz.writerow(self.__fieldnames4Hz)
        
#Appends data to the file created before
    def write100Hz(self):
        engineFrame100Hz = self.__dataFrame.getEngineFrame()
        wheelFrame100Hz = self.__dataFrame.getWheelSensorsFrame()
        gyroscopeFrame100Hz = self.__dataFrame.getGyroscopeFrame()
        FrameValues100Hz = [engineFrame100Hz["rpm"], engineFrame100Hz["tps"]]
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_x'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_y'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['accel_z'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_x'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_y'])
        FrameValues100Hz.append(gyroscopeFrame100Hz['gyro_z'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_fsx'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_fdx'])
        FrameValues100Hz.append(wheelFrame100Hz['potFAccuracy'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_rsx'])
        FrameValues100Hz.append(wheelFrame100Hz['pot_rdx'])
        FrameValues100Hz.append(wheelFrame100Hz['potRAccuracy'])
        FrameValues100Hz.append(wheelFrame100Hz['steeringEncoder'])
        # gpsFrameValues = list(self.__dataFrame.getGPSFrame().values())
        # wheelSensorsFrameValues = list(self.__dataFrame.getWheelSensorsFrame().values()) + 
        # gyroscopeFrameValues = list(self.__dataFrame.getGyroscopeFrame().values())
        
        self.__writerFile100Hz.writerow(FrameValues100Hz)

        # CLOSES THE FILE EVERY 500 WRITINGS
        self.__lineNumber100Hz = (self.__lineNumber100Hz + 1) % 500
        if (self.__lineNumber100Hz==0):
            self.__file100Hz.close()
            self.__file100Hz = open(self.__name100Hz, 'a', newline='')
            self.__writerFile100Hz = csv.writer(self.__file100Hz, delimiter=';', dialect='excel')


    def write10Hz(self):
        engineFrame10Hz = self.__dataFrame.getEngineFrame()
        FrameValues10Hz = [engineFrame10Hz["t_h20"], engineFrame10Hz["t_air"], engineFrame10Hz["t_oil"], engineFrame10Hz["vbb"], engineFrame10Hz["lambda1_avg"], engineFrame10Hz["lambda1_raw"], engineFrame10Hz["k_lambda1"], engineFrame10Hz["inj_low"], engineFrame10Hz["inj_high"]]
        
        self.__writerFile10Hz.writerow(FrameValues10Hz)
        
        # CLOSES THE FILE EVERY 50 WRITINGS
        self.__lineNumber10Hz = (self.__lineNumber10Hz + 1) % 50
        if (self.__lineNumber10Hz==0):
            self.__file10Hz.close()
            self.__file10Hz = open(self.__name10Hz, 'a', newline='')
            self.__writerFile10Hz = csv.writer(self.__file10Hz, delimiter=';', dialect='excel')
    
    def write4Hz(self):    
        FrameValues4Hz = []
        self.__writerFile4Hz.writerow(FrameValues4Hz)

        # CLOSES THE FILE EVERY 20 WRITINGS
        self.__lineNumber4Hz = (self.__lineNumber4Hz + 1) % 20
        if (self.__lineNumber4Hz==0):
            self.__file4Hz.close()
            self.__file4Hz = open(self.__name4Hz, 'a', newline='')
            self.__writerFile4Hz = csv.writer(self.__file4Hz, delimiter=';', dialect='excel')