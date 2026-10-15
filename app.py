from flask import Flask, render_template
from gpiozero import LED
app= Flask(__name__)
led=LED(17)
@app.route("/")
def home():
	return render_template("index.html")
	
@app.route("/on")
def turn_on():
	led.on()
	return "LED is ON"

@app.route("/off")
def turn_off():
	led.off()
	return "LED is Off"
	
app.run(host="0.0.0.0", port=5000, debug=False)

	
