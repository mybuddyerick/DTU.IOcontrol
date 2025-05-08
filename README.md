<div align="center">
  <img src="https://github.com/user-attachments/assets/9ea39d49-e732-4c1a-9bd7-f9d72f1e6d4d" alt="Logo" height="140">
</div>

<h1 align="center">02135 Introduction to Cyber Systems - Huzzah32 IO control</h1>

The assignment involves using a Feather Huzzah32 board and MicroPython to interact with various components including LEDs, buttons, a temperature sensor (MCP9808), and a potentiometer.

## Project Structure

- `main.py` – Entry point. Modify this file to import and run the task you want.
- `boot.py` – Initializes the board.
- `mcp9808.py` – Driver for the MCP9808 temperature sensor.
- `test1.py` to `test5.py` – Scripts for each task:
  - **Task 1**: Blink red LED while button is pressed.
  - **Task 2**: Cycle LEDs with button presses.
  - **Task 3**: Show temperature level with single LED.
  - **Task 4**: Show temperature level with RGB LED.
  - **Task 5**: Control Neopixel brightness with potentiometer.

## Hardware Requirements

- Feather Huzzah32 board
- MCP9808 temperature sensor
- 3x LEDs (green, yellow, red)
- RGB Neopixel LEDs
- Push buttons and 10K potentiometer
- Resistors: 330Ω (LEDs), 1kΩ (pull-up/down)

## How to Test

1. **Edit `main.py`** to import the desired task, e.g.:
   ```python
   from test5 import *  # Change to test1, test2, etc. as needed
   ```
2. Upload all files (`boot.py`, `main.py`, task scripts, and `mcp9808.py`) to the Huzzah32 using `ampy`, `rshell`, `Pymakr`, or `Thonny`.
3. Press the **reset button** on the board.
4. Observe the behavior according to the selected task and ensure the correct hardware is connected.

## Notes

- Use the correct I2C pins for the MCP9808 and include a pull-up resistor on SDA.
- Check whether the RGB LED is common-anode or cathode.
- Connect the potentiometer to an analog-capable pin for proper ADC readings.
