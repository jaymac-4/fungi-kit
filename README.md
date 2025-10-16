# Fungi Kit Repository

This repository contains all the code and lesson materials for the **Fungi Kit** project. It includes the Python scripts used with the Raspberry Pi Pico and the lesson plans needed to guide students through data collection, analysis, and visualisation activities.

---

## Before the Lesson

### 1. Prepare the Raspberry Pi Pico
Before starting the lesson:
- Copy **`main.py`** onto the Pico.
- The `ads1x15.py` driver file must be downloaded separately from  
  [https://github.com/robert-hh/ads1x15](https://github.com/robert-hh/ads1x15).  
- These files allow the Pico to collect sensor data and save it to `data.csv`.

You may also keep **`main_completed.py`** as a teacher reference file with all blanks filled in.

---

### 2. Prepare the Computer
- Copy **`fungi_kit_plotter.py`** to: C:\Users[Computer Name]\FungiKit\Documents
- This script reads and plots the sensor data recorded by the Pico.

---

## Using Thonny

1. Open **Thonny** as the Python IDE.  
2. Set the **interpreter** to **MicroPython (Raspberry Pi Pico)** when working on the Pico.  
3. To run the plotting script on the computer:
 - Change the interpreter back to **Local Python 3** in Thonny.  
 - Install the required libraries:
   - Open the **Tools → Manage plug-ins** menu.
   - Search for and install **matplotlib** and **pandas**.

---

## About the Code

### `main.py` (Student Version)
- Students complete this file during the lesson by filling in the missing values (e.g. pin numbers, I²C address, and channel numbers).  
- Once uploaded to the Pico, it:
- Reads sensor data from an ADS1115 via I²C.  
- Logs A0–A3 voltage readings to `data.csv`.  
- Blinks the on-board LED each time data is recorded.

### `main_completed.py` (Teacher Reference)
- A completed version of the same script with all fields filled in.  
- Useful for demonstration, testing, or troubleshooting.

### `fungi_kit_plotter.py`
- Runs on the local computer.  
- Reads `data.csv` created by the Pico.  
- Cleans the data by trimming early and late readings.  
- Uses **pandas** and **matplotlib** to graph voltage readings for each channel (A0–A3) over time.

---

## Lesson Resources

The **lesson_plan_pdfs** folder contains:
- **Wiring Guide** – explains hardware connections.
- **Programming Guide** – shows how to upload and run code on the Pico.
- **Plotting Guide** – covers data plotting and interpretation.

---

## Requirements Summary

### Hardware
- Raspberry Pi Pico (MicroPython installed)  
- ADS1115 ADC module  
- Jumper wires

### Software
- Thonny IDE  
- Matplotlib and Pandas installed via Thonny (Local Python 3)

---

## License

This project is provided for educational use.  
The `ads1x15.py` driver must be obtained separately from its original repository.
