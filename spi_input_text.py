from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import datetime

serial = spi(device=0, port=0)
device = ssd1306(serial)

text = input("Text to display: ")
delay = int(input("Run for X seconds: "))
time = datetime.datetime.now() + datetime.timedelta(seconds=delay)

while datetime.datetime.now() < time:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((58, 5), text, fill="white")
        draw.text((32, 10), "............", fill="white")
