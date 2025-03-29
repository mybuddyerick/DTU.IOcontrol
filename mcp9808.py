from machine import I2C
from micropython import const

# Default I2C address and register for temperature reading.
_MCP9808_DEFAULT_ADDRESS = const(0x18)
_MCP9808_REG_TEMP = const(0x05)

class MCP9808:
    def __init__(self, i2c: I2C, address: int = _MCP9808_DEFAULT_ADDRESS):
        """
        Initialize the MCP9808 temperature sensor.
        
        :param i2c: An initialized machine.I2C object.
        :param address: I2C address of the MCP9808 (default is 0x18).
        """
        self.i2c = i2c
        self.address = address

    def read_temperature(self) -> float:
        """
        Reads the temperature from the sensor and returns it in Celsius.
        
        The MCP9808 returns a 16-bit value from the temperature register.
        The lower 12 bits represent the temperature value. Multiply by 0.0625 to
        convert to Celsius. If the sign bit (bit 12) is set, subtract 256.
        """
        # Read 2 bytes from the temperature register.
        data = self.i2c.readfrom_mem(self.address, _MCP9808_REG_TEMP, 2)
        # Combine the two bytes.
        raw = (data[0] << 8) | data[1]
        # Extract the lower 12 bits.
        temp = raw & 0x0FFF
        # Multiply by resolution to get Celsius.
        temp_c = temp * 0.0625
        # If the sign bit is set, subtract 256 to get negative temperature.
        if raw & 0x1000:
            temp_c -= 256
        return temp_c

    @property
    def temperature(self) -> float:
        """
        Property to get the current temperature in Celsius.
        """
        return self.read_temperature()
