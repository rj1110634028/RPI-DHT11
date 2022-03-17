import Adafruit_DHT 
import paho.mqtt.client as mqtt
import json  
import datetime 
import time

# 設置日期時間的格式
ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'

# 連線設定
# 初始化地端程式
client = mqtt.Client()

# 設定登入帳號密碼
client.username_pw_set("pi","00000000")

# 設定連線資訊(IP, Port, 連線時間)
client.connect("192.168.168.109", 1883, 60)

DHT_SENSOR = Adafruit_DHT.DHT11 
DHT_PIN = 4  

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    if humidity is not None and temperature is not None:
        t = datetime.datetime.now().strftime(ISOTIMEFORMAT)
        temp = temperature
        hum = humidity
        payload = {'Temperature' : temp , "Humidity": hum , 'Time' : t}
        print (json.dumps(payload))
        #要發布的主題和內容
        client.publish("Try/MQTT", json.dumps(payload))
        time.sleep(3)
    else:
        print("Failed to retrieve data from HDT22 sensor")
        