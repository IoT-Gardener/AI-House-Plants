# AI_House_Plants
When you have loads of house plants watering them can be a chore, and when they all need different amounts of water, and different conditions it becomes almost unmanageable! 

However through the use of remote sensors, the internet of things, a small database, and a splash of machine learning this problem can be *easily* overcome!

## How it works... currently
At the moment There are 3 main steps to the process.
- Step 1: An Arduino with a soil moisture sensor publishes soil moisture readings to serial
- Step 2: A python script reads the values published to serial and adds them to a NoSQL database (mongoDB)
- Step 3: A streamlit app reads the values from the database and plots a lovely graph!

## Future Plans
Lots... CI/CD pipeline, MLOps Pipeline, better data solution than writing and reading directly from a mongoDB

Immediate next steps are to train a basic model that will classify whether a plant needs watering or not based on sensor data and flag the need for watering in the webapp.

## Setup
### Software and tools
I used VS code and the arduino IDE to develop and run this project, you can find the installation for [VS code here](https://code.visualstudio.com/) and the [Arduino IDE here](https://www.arduino.cc/en/software) 

### Setting up the Arduino
... coming soon...

### Python virtual environment
In order to work out of a clean environment I recommend using a python virtual environment.

All of the following commands should be run in a terminal on a machine with python installed, a python download can be found [here](https://www.python.org/downloads/).
1) Create the virtual environment:
```
$py -m venv venv
```
2) Activate the virtual enviornment:
```
.\.venv\Scripts\activate
```
3) Done. It is as easy as that!
Bonus step is to install of all the required python packages from the requirements.txt
- Install the requirements:
```
pip install -r requirements.txt
```

### Running the apps
To get this working you will need to run the monitoring and logging app to populate the database, and the streamlit app to view the flashy webpage!
1) Run the app
```
python src/monitor_and_log.py
```
2) Run the streamlit app
```
streamlit run src/streamlit_app.py
```
