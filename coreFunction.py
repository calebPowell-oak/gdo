import time
import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   23 : {'name' : 'GPIO 23', 'state' : GPIO.LOW},
   24 : {'name' : 'GPIO 24', 'state' : GPIO.LOW}
   }

# Set each pin as an output and make it low:
for pin in pins:
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, GPIO.LOW)

# Set base route
baseUrl = "/api"

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route(baseUrl + "/pin/<changePin>")
def action(changePin):
   # Convert the pin from the URL into an integer:
   changePin = int(changePin)
   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']
   # If the action part of the URL is "on," execute the code indented below

   GPIO.output(changePin, GPIO.HIGH)
   time.sleep(0.1)
   GPIO.output(changePin, GPIO.LOW)
   message = "Activated " + deviceName

   return 0

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=5000, debug=True)
