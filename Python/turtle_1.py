import random
import os
from paho.mqtt import client as mqtt_client
import pyautogui
import time 



# MQTT broker details
broker = '192.168.3.33'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'




def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribeShortcut(client: mqtt_client, topic: str):
    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        print(f"Received `{payload}` from `{msg.topic}` topic")
        
        if payload == "tab":
            print("Opening browser tab...")
            open_browser()
        elif payload == "screenshot":
            print("Opening snipping tool...")
            make_screenshot()
        elif payload == "lock":
            print("Locking the screen...")
            lock_screen()
        elif payload == "take_picture":
            print("Taking a picture...")
            take_picture()
        else:
            print("Invalid command")


       


    client.subscribe(topic)
    client.on_message = on_message

def send(client: mqtt_client, topic: str, message: str):
    result = client.publish(topic, message)
    status = result[0]
    if status == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic `{topic}`")

def open_browser():
    # Command to open the default web browser on Linux
    command = "start www.google.com"  # Replace with your URL
    os.system(command)

def make_screenshot():
    command =  "start snippingtool.exe"
    os.system(command)

def lock_screen():
    command = "rundll32.exe user32.dll,LockWorkStation"
    os.system(command)

def take_picture():
    command = "start microsoft.windows.camera:"
    command2 = "taskkill /im WindowsCamera.exe /t /f"
    os.system(command)
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(0.2)
    os.system(command2)
    
    
    
def run():
    
    client = connect_mqtt()
    client.loop_start()

    # Subscribe to a topic
    subscribeShortcut(client, "IOE/widmerroger/shortcuts")

    try:
        # Keep the main thread running to maintain the subscription
        while True:
            pass
    except KeyboardInterrupt:
        print("Stopping...")
        client.loop_stop()
        client.disconnect()

if __name__ == '__main__':
    run()
