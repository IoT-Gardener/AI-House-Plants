import serial
import time
from pymongo import MongoClient

# Define mongodb details
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'Test'
COLLECTION_NAME = 'Test'

if __name__ == "__main__":
    print("Hello world!")

    # Connect to the mongo client and db/collection
    connection = MongoClient(MONGODB_HOST, MONGODB_PORT)
    collection = connection[DB_NAME][COLLECTION_NAME]

    # Connect to the serial port the arduino is publishing the sensor data to
    ser = serial.Serial('COM3', 9600, timeout=1)
    
    # Loop infinitely
    while True:
        try:
            # Read the sensor reading from serial
            sensor_reading = float(ser.readline().decode().strip())

            # Print the sensor reading
            print(sensor_reading)

            # Check the value has been correctly read and has a reasonable value
            if sensor_reading > 100:
                # Log the sensor data to mongodb
                collection.insert_one({
                    "SensorID":"M001",
                    "Type": "Soil_Moisture",
                    "Reading": sensor_reading
                })
        except:
            print("Uhoh!")