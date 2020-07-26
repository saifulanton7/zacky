import serial
import json
from time import sleep
from firebase import firebase
from time import sleep

url = "https://pertamini-37a49.firebaseio.com/"

firebase = firebase.FirebaseApplication(url, None)


firebase.put("/", "/Flow", "1890")

def sendFirebase(path, data):
        firebase.put("/", path, data)

ser = serial.Serial("/dev/ttyACM0",9600)

def getSerial():
	if(ser.readline()!=""):
		a = ser.readline()
		a = a.replace("\r\n","")
		print(a)
		y = json.loads(a) 
	       	sendFirebase("/Ultrasonic/Persediaan",str(y["Persediaan"]))
        	sendFirebase("/Ultrasonic/Penyaluran",str(y["Penyaluran"]))
        	sendFirebase("/Flow",str(y["Flow"]))
	sleep(0.5)
def main():
	getSerial()

if __name__ == '__main__':
    try:
	while(True):
	        main()
    except KeyboardInterrupt:
        exit()

