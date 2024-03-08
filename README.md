![Silly little header image for this project](https://github.com/hugmouse/ESP32-ST7789-Micropython/assets/44648612/bb7c42e6-5dbc-445a-92be-465b562649be)

# ESP32 + ST7789 + Micropython

Just a little experiment with ST7789 240x240px display, includes bare-bones SPI display driver.

## Requirements

- An ESP32/Wroom microcontroller
- A ST7789 240x240px display
- [MicroPython firmware installed on the ESP32](https://docs.micropython.org/en/latest/esp32/tutorial/intro.html)

## Hacking

I was writing this code in REPL, so just copy and paste all the stuff from `main.py` into your micropython repl and you
good to go!

Make sure to replace those variables though:

```python
scl_pin = REPLACE
sda_pin = WITH
res_pin = YOUR
dc_pin = PINS
```

Example usage:

```python
def rainbow_cycle():
    """
    Cycles through rainbow colors and displays it on the screen!
    """
    rainbow_colors = [
        0xF800,  # Red
        0xFC00,  # Orange
        0xFFE0,  # Yellow
        0x07E0,  # Green
        0x001F,  # Blue
        0x781F,  # Indigo
        0x780F,  # Violet
    ]

    for color in rainbow_colors:
        fill_color_chunked_optimized(color)
```

Example output:

https://github.com/hugmouse/ESP32-ST7789-Micropython/assets/44648612/0460be67-5945-4e37-893e-375386ff3d4d

## Other stuff

- [ST7789 Datasheet](https://www.waveshare.com/w/upload/a/ae/ST7789_Datasheet.pdf)