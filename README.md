# Weather API Python Program
This is a simple Python program that uses the Weather API to retrieve the current weather data for a given city and outputs the temperature to the console and speaks it aloud using the espeak command.

## Requirements
- Python 3
- requests library
- espeak command (Linux)

## Usage
To use the program, follow these steps:

- Clone or download the program files from the GitHub repository.
- Install the requests library by running the command pip install requests in your terminal.
- Install espeak command if not already installed. To install espeak on Ubuntu, run the command sudo apt-get install espeak in your terminal.
- Open a terminal window and navigate to the directory where you saved the program files.
- Run the program using the command python3 weather.py.
- Enter the name of the city you want to retrieve the current weather data for.
- The current temperature in Celsius for the city will be output to the console and spoken aloud using the espeak command.
Using on Windows
- This program was built on Linux, but it can be used on Windows as well. To use this program on Windows, you may need to install a Unix-like environment such as Cygwin or WSL.


# Follow these steps to use this program on Windows:

- Install Python 3 on your machine by downloading it from the official website: https://www.python.org/downloads/
- Install the requests library by running the command pip install requests in your command prompt.
- Install espeak command on your system using the installer available at https://github.com/espeak-ng/espeak-ng/releases.
- Open a command prompt by pressing Win + R, typing cmd, and hitting Enter.
- Navigate to the directory where you have saved the weather.py file.
- Run the program using the command python weather.py.
- Enter the name of the city you want to retrieve the current weather data for.
- The current temperature in Celsius for the city will be output to the console and spoken aloud using the espeak command.

### Note
The espeak command may not work on some systems due to differences in audio drivers. If you encounter issues with the espeak command, you can comment out the following line in the code:

- python
- Copy code
- os.system(f"espeak 'The current weather is in {city} is {w} degrees'")
### This will prevent the program from attempting to use the espeak command.
