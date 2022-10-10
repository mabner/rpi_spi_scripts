from luma.core.interface.serial import i2c, spi, pcf8574
from luma.core.interface.parallel import bitbang_6800
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1309, ssd1325, ssd1331, sh1106, ws0010

serial = spi(device=0, port=0)

device = ssd1306(serial)
repeat = 1

text =  input("Text to display:")

while repeat == 1:
	with canvas(device) as draw:
    		draw.rectangle(device.bounding_box, outline="white", fill="black")
    		draw.text((30, 40), text, fill="white")

