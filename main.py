# Import libraries
from machine import I2C, Pin
from ads1x15 import ADS1115
import time

# 1. Set up the I2C connection
# (This connects your Pico to the sensor)
# The SDA pin used in the wiring guide is pin 0
# The SCL pin used in the wiring guide is pin 1
i2c = I2C(0, sda=Pin(___), scl=Pin(___))

# 2. Set up the ADC (the sensor that reads voltages)
# The address for the ADC is 72
adc = ADS1115(i2c, address=___, gain=0)

# 3. Set up the LED
# The LED is on pin 25
led = Pin(___, Pin.OUT)

# 4. Create a CSV file to store data
#    "a" means append — keep adding new data to the file
with open("data.csv", "a") as f:
    f.write("timestamp,A0,A1,A2,A3\n")

# 5. Function to save data to the file
def log_data_to_csv(A0, A1, A2, A3):
    with open("data.csv", "a") as f:
        timestamp = time.time()   # Get current time
        # Write one line of data to the file
        f.write(f"{timestamp},{A0},{A1},{A2},{A3}\n")

# 6. Main loop (runs forever)
while True:
    # Read from each sensor channel (0, 1, 2, 3)
    # Fill in the blanks below with a number for each channel
    A0 = adc.read(4, ___)
    A1 = adc.read(4, ___)
    A2 = adc.read(4, ___)
    A3 = adc.read(4, ___)

    # Convert the raw readings to voltage
    # We need to convert the variables above into readable data
    # Fill in the blanks below with the variables above to
    # convert the raw values to a voltage
    A0_v = adc.raw_to_v(___)
    A1_v = adc.raw_to_v(___)
    A2_v = adc.raw_to_v(___)
    A3_v = adc.raw_to_v(___)

    # Print the readings (to check they work)
    print(A0_v, A1_v, A2_v, A3_v)

    # Save the readings to the file
    log_data_to_csv(A0_v, A1_v, A2_v, A3_v)

    # Blink the LED once
    led.value(1)       # Turn LED on
    time.sleep(0.1)    # Wait a short time
    led.value(0)       # Turn LED off

    # Wait before reading again for a total of 1 second
    time.sleep(0.9)
