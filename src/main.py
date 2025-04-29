import time
import board
import neopixel

# Set up the onboard NeoPixel
pixel = neopixel.NeoPixel(board.NEOPIXEL, 1)

# Main loop
while True:
    pixel[0] = (0, 255, 0)  # Green
    time.sleep(0.5)
    pixel[0] = (0, 0, 0)    # Off
    time.sleep(0.5)
