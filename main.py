import machine
import utime

scl_pin = REPLACE
sda_pin = WITH
res_pin = YOUR
dc_pin = PINS

# SPI initialization
spi = machine.SPI(2, baudrate=26600000, sck=machine.Pin(scl_pin), mosi=machine.Pin(sda_pin),
                  miso=None, polarity=1, phase=1)

# GPIO pins for RES and DC initialized as output
res = machine.Pin(res_pin, machine.Pin.OUT)
dc = machine.Pin(dc_pin, machine.Pin.OUT)


def reset_display():
    """
    Resets the display.
    """
    res.value(1)
    utime.sleep_ms(5)
    res.value(0)
    utime.sleep_ms(20)
    res.value(1)
    utime.sleep_ms(150)


def send_command(command, data=None):
    """
    Sends a command to the display.

    :param command: The command byte.
    :param data: Optional; bytes of data to send after the command.
    """
    dc.value(0)  # Set DC to command mode
    spi.write(bytearray([command]))
    if data is not None:
        dc.value(1)  # Set DC to data mode
        spi.write(bytearray(data))
    dc.value(0)  # Reset DC to command mode


def init_display():
    """
    Initializes the display.
    """
    reset_display()
    send_command(0x11)                      # Sleep out
    utime.sleep_ms(120)
    send_command(0x20)                      # Display inversion off
    send_command(0xB3, [0x01, 0x00, 0x00])  # Frame rate control
    send_command(0xC0, [0x0c])              # LCM Control
    send_command(0x36, [0x00])              # Memory Data Access Control
    send_command(0x3A, [0x55])              # Interface Pixel Format
    send_command(0x29)                      # Display ON


def fill_color_chunked_optimized(color):
    """
    Fills the display with a solid color.

    :param color: The color value to fill.
    """
    width, height = 240, 240
    total_pixels = width * height
    chunk_size = 4800
    color_high, color_low = color >> 8, color & 0xFF
    buf = bytearray([color_high, color_low] * chunk_size)

    # Set column and row address just once for the whole screen
    send_command(0x2A, [0x00, 0x00, 0x00, 0xEF])
    send_command(0x2B, [0x00, 0x00, 0x00, 0xEF])
    send_command(0x2C)  # Start frame memory write

    dc.value(1)
    for _ in range(total_pixels // chunk_size):
        spi.write(memoryview(buf))

    dc.value(0)
