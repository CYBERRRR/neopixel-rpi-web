from flask import Flask, render_template, request
import time
import board
import neopixel

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 150

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

app=Flask(__name__)

def allColor(red, green, blue):
	pixels.fill((red, green, blue))
	pixels.show()

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/set_color", methods=['POST'])
def set_color():
	rgb = request.get_json()
	red = rgb['r']
	green = rgb['g']
	blue['b']
	allColor(red, green, blie)
	return render_template('index.html'), 204

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80, debug=True)
