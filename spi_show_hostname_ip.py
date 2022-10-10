from textwrap import fill
from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1306
import socket
from pynat import get_ip_info

serial = spi(device=0, port=0)
device = ssd1306(serial)

# Hostname
hostname = socket.gethostname()

# Internal IP
ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip.connect(("0.0.0.0", 80))

# External IP
topology, ext_ip, ext_port = get_ip_info()

while True:
    print(hostname)
    print("---------------------")
    print(ip.getsockname()[0])
    print("---------------------")
    print(ext_ip)
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((5, 5), hostname, fill="white")
        draw.text((0, 10), "---------------------", fill="white")
        draw.text((5, 15), ip.getsockname()[0], fill="white")
        draw.text((0, 20), "---------------------", fill="white")
        draw.text((5, 25), ext_ip, fill="white")
