from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import socket

serial = spi(device=0, port=0)
device = ssd1306(serial)

hostname = socket.gethostname()

while True:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((5, 5), hostname, fill="white")
        draw.text((0, 10), "---------------------", fill="white")
