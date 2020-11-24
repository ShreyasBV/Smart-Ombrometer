import conf, requests, math, time, json
from boltiot import Sms, bolt

value1 = 20
value2 = 500
value3 = 1500
value4 = 500

data = []             #to empty the list for storing value
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mybolt.digitalWrite(0,"LOW")

def get_sv(pin):
    try:
        response = mybolt.analogRead(pin)
        data = json.loads(response)
        if data["success']!=1:
            print("Request Failed")
            print("Response", data)
            return -999
        sensor_value = int(data["value"])
        return sensor_value
    except Exception as e:
        print("Error")
        print(e)
        return -999
        
while True:
    print("Reading Sensor Value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("Sensor value is " + str(data['value']))
    try:
        sensor_value = int(data['value'])
        if sensor_value < value4:
            mybolt.digitalWrite(0,"LOW")
        elif sensor_value > value2 or sensor_value < value3:
            print("Making request to TWILIO to sens SMS")
            value = (sensor_value/20)
            response = sms.send_sms("The amount of rainfall is: " +str(value))
            print("Response recieved from TWILIO is: " +str(response_status))
            mybolt.digitalWrite(0,"HIGH")
        elif sensor_value > value1 or sensor_value < value2
            print("Making request to TWILIO to send SMS")
            value = (sensor_value/20)
            response = sms.send_sms("The amount of rainfall is: " +str(value))
            print("Response recieved from TWILIO is: " +str(response_status))
            mybolt.digitalWrite(0,"LOW")
    except Exception as e:
        print("Error")
        print(e)
    time.sleep(10)