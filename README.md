# How to make a weather app using Python:

In this note, we will work on two Python scripts, backend.py and frontend.py. Let’s begin with the most important part, the backend.

Before we get started, open up your favorite or one of your code editors, as you cannot use GitHub Codespaces. Options are VSCode, PyCharm, and you may also use Sublime Text.
Any other code editor will work, as Jupyter Notebooks-like editors will not work, such as JupyterLab, Jupyter Notebook, and Google Colab.

When you are ready, read on.

## Creating the Backend:

Before we start with this topic, make sure you have created a file called backend.py.

### Step 1:
Get all required modules or Python libraries; the ones we will use are requests, pandas, and the datetime library. Go ahead and import them. If they are not imported or installed, run this command in your code editor terminal or Command Prompt:
```
pip install requests, pandas, datetime
```

This is how it should look in your code:
```
import requests
import pandas as pd
from datetime import datetime
```
Those modules are the main thing in this code, as without them, this code would be impossible to make.
### Step 2:
	
 Get the API’s URL and its encoding map.

The api we are going to use is “https://api.open-meteo.com/v1/forecast” - (Open-Meteo)
Put that string link inside a variable called BASE_URL

The weather code map is provided below, as well as how you should set the BASE_URL variable:
```
BASE_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODE_MAP = {
    0: "Sunny (Clear sky)",
    1: "Sunny (Mostly clear)",
    2: "Partly cloudy",
    3: "Cloudy sky",
    45: "Foggy weather",
    48: "Less foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Little snow",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Mild thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}
```


This piece of code here represents the decoding of the weather code, such as if the code was 3, what would it be? The variable up there in BASE_URL is where we will request from the API.

Question: Do we use the requests library (Search it on Google - Click Here) we imported in Step 1 to request the BASE_URL

Answer: Yes, that is the purpose of the requests library: to get data from an API and return the outcome (status code) of the request, just like the code below:
```
import requests


# This is an example.


eg_response = requests.get('https://example.com', params="parameters")
eg_response.raise_for_status()
```

### Step 3:
	You will create the backend function meant for when the frontend.py is completed.

You will create a ‘def’ function to get the weather in this step. The function is meant for when you want to do the frontend (frontend.py), as in this example, where the backend is the backend.py file. In this case, you can import the file if you are using any of the three code editors I listed above.
```
# The below code is an Example! Do not put this code in backend.py or
# frontend.py 

from example import example_function


example_function()
```
What should be added to backend.py is below (Remember, repetition of same lines of code shouldn't be repeated since it shows part of the code around the new ones)

def getHourlyWeather():

Now, let’s get to work on our main point in the code.

### Step 4:

We will create a try-except block, input our latitude and longitude for the place in two variables, LAT = latitude, and LON = longitude, and then put in the parameters, or data we want to fetch from the API, using significant data the API (website), recognizes. 

The parameters will include:

. Latitude and Longitude
. The time forecast zone, with the data in there
. Timezone
. Forecast days
. And the past days (optional)

What should be added to backend.py is below (Remember, repetition of same lines of code shouldn't be repeated since it shows part of the code around the new ones)
vars = variables
```
# Includes the def function itself below


def getHourlyWeather():
    try:
	  # Example for London
        LAT = 51.5074
        LON = 0.1278


        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode", # Time type, 2 vars
            "timezone": "auto",
            "forecast_days": 15, # How many days into the future
            "past_days": 1, # To show the current day
            "temperature_unit": "fahrenheit"
        }


```


Question: Why are we typing this part?

Answer: We are typing this part because we need to get data, and there is no other way to get the data, than typing what we want from the data, because no inputs would input in an error and the data will not know what to give us, but it won’t crash since we are using block that you can use to stop errors from happening, but display your own error.

### Step 5: 

The next part of the code is where we finally use the requests library, for requesting from BASE_URL, which we declared to be Open-Meteo in Step 2. The way we are using it is exactly just like the example in Step 2 also.
```
import requests


# This is an example.


eg_response = requests.get('https://example.com', params="parameters")
eg_response.raise_for_status()
```
Example from Step 2 above.

What should be added to backend.py is below (Remember, repitition of same lines of code shouldn't be repeated since it shows part of the code around the new ones)

⚠️ Warning: This is part of inside the def ‘getHourlyWeather()’ function. Don’t remove the function as it is still used.
```
        LAT = 6.4183
        LON = 2.88132


        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode",
            "timezone": "auto",
            "forecast_days": 15,  
            "past_days": 1,
            "temperature_unit": "fahrenheit"
        }


        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Optional
        model = response.json()
```
Question: Why is the requests library set up like this?

Answer: It is like this because in the requests library, you use the get keyword to get an API’s URL, and the data you want to get from it. The line under the first declaration of the response variable is optional, as it shows the status code that was passed. The model variable is declared to have the response data that we required using the params, and changes it into JSON (Search it on Google - Click here) format.


### Step 6:
Make sure all data you need is included, and create variables for time type, temperature, and weather code.

In this step, you will create a if-else statement to check if all data is brought, and four variables:

Create an if statement that shows if  string hourly is not in the model variable or string temperature_2m is not in variable model dictionary ‘hourly’ or string weathercode is not in model dictionary value ‘hourly’, it should return this value: "Error: Missing 'hourly' data in the model."


Make a variable called hourly_forecast and set it to the variable model’s dictionary value ‘hourly’
Make a variable called times and set it to the variable hourly_forecast’s dictionary value ‘time’
Make a variable called temperatures and set it to the variable hourly_forecast’s dictionary value ‘temperature_2m’
Make a variable called hourly_forecast and set it to the variable hourly_forecast’s dictionary value ‘weathercode’

What should be added to backend.py is below (Remember, repitition of same lines of code shouldn't be repeated since it shows part of the code around the new ones)
```
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        model = response.json()


        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."


        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]
```
Right now, take a 5 minute break and then see the full code together, as we are not done but this is a checkpoint for you to see the code so far.
```
import requests
import pandas as pd
from datetime import datetime


BASE_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODE_MAP = {
    0: "Sunny (Clear sky)",
    1: "Sunny (Mostly clear)",
    2: "Partly cloudy",
    3: "Cloudy sky",
    45: "Foggy weather",
    48: "Less foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Little snow",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Mild thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}


def getHourlyWeather():
    try:
        LAT = 6.4183
        LON = 2.88132


        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode",
            "timezone": "auto",
            "forecast_days": 15,  
            "past_days": 1,
            "temperature_unit": "fahrenheit"
        }


        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        model = response.json()


        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."


        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]
```

⚠️ Warning: Do not run this code, as you will run it when you finish, because currently, it will output an error.

In the next step, we will use another library, the datetime library to create a variable and put the current date in string format in that variable.

### Step 7:
Now that we are here, let us create a variable called current_date and put the current date in string format in that variable using the datetime library (Search it on Google - Click Here). We will also create two new list variables, one called today_data and the other called future_data.

To do this, create a variable named current_date and set it to this value: datetime.now().strftime("%Y-%m-%d")
Let me explain what we just did up there. In the beginning of the line, we put this: datetime.now().  <- Get the current date and time for the current day.
strftime("%Y-%m-%d") <- Convert the datetime value to a string. %Y = Year, %m = Month, %d = Day

The new variable should be added to the code like this:
        current_date = datetime.now().strftime("%Y-%m-%d")

The reason for it’s indentation is because every piece of code under the def getHourlyWeather(): is inside that function. If you didn’t indent it, select everything under the def getHourlyWeather(): and use Ctrl+] pair to indent it with 4 spaces. If you accidentally indented it more than once, use Ctrl+[ pair to unindent by 4 spaces.

The next thing to do is to create two new lists one with the variable name today_data, and the other future_data. This should be really easy, but just in case, here is that code added to the backend.py. 
```
        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."


        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]


        current_date = datetime.now().strftime("%Y-%m-%d")
	  # Add this piece below if not already added
        today_data = []
        future_data = []
```

🎉🎊🥳
 CoNgRaTuLaTiOnS! You have made it past more than half the code in backend.py.

Take a stretch and come back in. 🙆🧘

### Step 8:
[i] is for iterating, you could use any variable.

Create a for-loop to decode the weather with the WEATHER_CODE_MAP dictionary variable, and put a value like ‘Unknown’ for the unknown codes. 

Iterate with any variable, but I will choose a default ‘i’. Put the range in the length of times, and in the for-loop, make two variables, date and hour, to represent the time and the day. They will be split upon the times[i].split(“T”). 

The next variable will be weather, which would use the WEATHER_CODE_MAP to decode it to get the weather, and [i] again for iterating through, and each unknown code will be ‘Unknown’, although you can use your own. 

Next will be to make a variable called temp, that is equal to temperature[i]. After that, create an if-statement to see if the date variable is equal to the current_date variable.
If so, add these four list attributes to today_data, date, hour, weather, f”{temp}F”
If not, add the same four list attributes to future_data list variable.

Current added code into getHourlyWeather function:
```
        current_date = datetime.now().strftime("%Y-%m-%d")


        today_data = []
        future_data = []
        
        # Below is added code.
        for i in range(len(times)):
            date, hour = times[i].split("T")
            weather = WEATHER_CODE_MAP.get(weather_codes[i], "Unknown")
            temp = temperatures[i]
            if date == current_date:
                today_data.append([date, hour, weather, f"{temp}°F"])
            else:
                future_data.append([date, hour, weather, f"{temp}°F"])
```
### Step 9:
 In this area, we will now add the last section of code for backend.py. This piece of code, or step, will be consisting of two new variables: today_df, and future_df. We will give them a dataframe value, which is like an array or list. 

After all above, we will make our return statement, to return those two variables, today_df, and future_df, but in a way that the user can understand the reason for the data. Like bringing in a string. 

Can you do it before seeing the code below? It might not look exactly the same, but give it a try. 

Then we will create at last, our except part of the code, as it will occur with an Error, or in python, an Exception. Then you want to return that error through the exception.

Question: Does the ‘df’ in those two variables correspond to the pandas library? Is that why we imported it?

Answer: Yes, because the most popular reason everyone recognizes pandas is for it’s dataframe and ability to read other files, but in this step, we are only using it to create a dataframe.

If you’ve tried the code, here is how the last piece should look:
```
            if date == current_date:
                today_data.append([date, hour, weather, f"{temp}°F"])
            else:
                future_data.append([date, hour, weather, f"{temp}°F"])
 		# All above this comment shouldn’t be repeated. Including code
		# not showing.
        today_df = pd.DataFrame(today_data, columns=["Date", "Hour", "Weather", "Temperature"])
        future_df = pd.DataFrame(future_data, columns=["Date", "Hour", "Weather", "Temperature"])


        return "Today\n\n" + today_df.to_string(index=False) + "\n\nNext 15 days\n\n" + future_df.to_string(index=False)
    except Exception as e:
        return f"An error occurred: {e}"
```
As you can see, the code shows all of the variables. Now put this in if you haven’t. Now, let’s move to frontend.py. We will first show the full code.
```
import requests
import pandas as pd
from datetime import datetime


BASE_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODE_MAP = {
    0: "Sunny (Clear sky)",
    1: "Sunny (Mostly clear)",
    2: "Partly cloudy",
    3: "Cloudy sky",
    45: "Foggy weather",
    48: "Less foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Little snow",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Mild thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}


def getHourlyWeather():
    try:
        LAT = 6.4183
        LON = 2.88132


        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode",
            "timezone": "auto",
            "forecast_days": 15,  
            "past_days": 1,
            "temperature_unit": "fahrenheit"
        }


        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        model = response.json()


        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."


        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]


        current_date = datetime.now().strftime("%Y-%m-%d")


        today_data = []
        future_data = []
        for i in range(len(times)):
            date, hour = times[i].split("T")
            weather = WEATHER_CODE_MAP.get(weather_codes[i], "Unknown")
            temp = temperatures[i]
            if date == current_date:
                today_data.append([date, hour, weather, f"{temp}°F"])
            else:
                future_data.append([date, hour, weather, f"{temp}°F"])


        today_df = pd.DataFrame(today_data, columns=["Date", "Hour", "Weather", "Temperature"])
        future_df = pd.DataFrame(future_data, columns=["Date", "Hour", "Weather", "Temperature"])


        return "Today\n\n" + today_df.to_string(index=False) + "\n\nNext 15 days\n\n" + future_df.to_string(index=False)
    except Exception as e:
        return f"An error occurred: {e}"
```
Now that we are done with backend.py, let’s move to frontend.py.


## Building the Frontend:

In this topic, we will now build the frontend. The frontend code is only 5 steps long, as it involves some functions that are essential. Before getting started, just like in the previous topic, we obviously and should have created a file for the backend. Now do the same thing, just this time, call it frontend.py.

### Step 1:
Import required modules.

Just as in the step 1 of the backend, we got the libraries needed. So now, I will provide you the pip for getting the libraries, and we will import our last python file.
```
pip install tkinter
```
In the line above, you can see the only thing installed was tkinter, the reason: That is the only library needed to create a simple frontend. The other thing we will need is the backend.

How exactly do we get our backend.py file into our frontend.py file? We call the from and write the name of the file we want to import, which is backend.py, but, without the .py included in it. Then, use import and add a function, variable or what ever we want to import. You will import the getHourlyWeather, without the brackets included.

Code view:
```
import tkinter as tk
from tkinter import scrolledtext
from backend import getHourlyWeather
```


Now that you have typed those lines of code, let’s move on.

### Step 2:
Let’s plan ahead and create the 3 functions needed for this frontend.py. This is a big step, so we’ll split it into 3 parts.

#### Part 1:
We will create the first function, display_weather(), as it will include a global variable called weather_data, and the weather_data variable is set to the value the return statement made in getHourlyWeather(), since we had imported the file in. Then, we will display the variable with the next function we will create, display_text()

Code: 
```
import tkinter as tk
from tkinter import scrolledtext
from backend import getHourlyWeather


def display_weather():
    global weather_data
    weather_data = getHourlyWeather()
    display_text(weather_data)
```
#### Part 2:
	
We will now create the second function: the display_text function. This function will display what is put into it in a text_area. Don’t worry about the text_area variable, as it will be declared after all the functions have been made.
#### Part 3:
This function called search_by_date(), will be used for searching the data to look for a specific day. You will use an if statement to check if there is the weather_data variable, else it should show something like no data available, or click the button, or a message to notify the user. 

If there is the weather_data variable, make a variable called search_date and let it equal to a variable called search_entry.get().strip(), which is getting the data from that variable, and removing whitespace, or spaces in it.

If there is no value for the search_date variable, make an if statement to handle this and provide the user a message to let them know.

Next up, is filtering the code, such as removing all left whitespace or spaces, just to make sure it is all gone, and all extra ‘-’ for marking a date. The best option for remove those things out is the replace, so you don’t just cause more problems, but you can change the value.

After that, join lines of strings on to a variable called filtered_data. Then use an if statement to check if there is data to present. If there is, it would use the same display_text function to display it, else use the display_text function, as you should have always used, to show the message to the user on the frontend.


Code for all functions so far:
```
import tkinter as tk
from tkinter import scrolledtext
from backend import getHourlyWeather


def display_weather():
    global weather_data
    weather_data = getHourlyWeather()
    display_text(weather_data)


def display_text(text):
    text_area.config(state="normal")  
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)
    text_area.config(state="disabled")


def search_by_date():
    if not weather_data:
        display_text("No weather data available. Please click the button to get the weather.")
        return


    search_date = search_entry.get().strip()
    if not search_date:
        display_text("Please enter a valid date (e.g., 2025-05-07).")
        return


    search_date = search_date.replace(' ', '-')
    search_date = search_date.replace('--', '-')


    filtered_data = "\n".join(
        line for line in weather_data.split("\n") if search_date in line
    )
    if filtered_data:
        display_text(filtered_data)
    else:
        display_text(f"No data found for the date: {search_date}")
```

### Step 3:
	In here, we will quickly show you the code needed for the app, but let’s explain it.

1. Setup: 
	Import the necessary libraries: tkinter for the GUI, datetime for date handling, and requests (or similar) to fetch data from a weather API.
2. Main Application Window: 
	Create the main window using Tk() and set a title (e.g., "Weather App").
3. Fetch Weather Data Button: 
	Create a button with text like "Fetch Weather".
	When clicked, this button should call a function (e.g., fetch_weather()) to:
	Get the current location (Specified Latitude and Longitude location)
	Fetch weather data using the weather API.
	Display the data in a scrollable text area.
4. Scrollable Text Area: 
	Use the scrolledtext widget to create a text area that can be scrolled when the content exceeds its visible bounds.
	Update this text area with the weather information fetched from the API.
5. Search Bar:
	Create a label (e.g., "Search by Date:"). 
	Create an entry field (a single-line text box) for the user to type in a date. 
	Create a button with text like "Search". 
	When clicked, this button should call a function (e.g., search_by_date()) to:
	Get the date entered by the user. Filter the weather data by date and display it in the text area.

# Review: 
## Full Frontend code:
```
import tkinter as tk
from tkinter import scrolledtext
from backend import getHourlyWeather


def display_weather():
    global weather_data
    weather_data = getHourlyWeather()
    display_text(weather_data)


def display_text(text):
    text_area.config(state="normal")  
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, text)
    text_area.config(state="disabled")


def search_by_date():
    if not weather_data:
        display_text("No weather data available. Please click the button to get the weather.")
        return


    search_date = search_entry.get().strip()
    if not search_date:
        display_text("Please enter a valid date (e.g., 2025-05-07).")
        return


    search_date = search_date.replace(' ', '-')
    search_date = search_date.replace('--', '-')


    filtered_data = "\n".join(
        line for line in weather_data.split("\n") if search_date in line
    )
    if filtered_data:
        display_text(filtered_data)
    else:
        display_text(f"No data found for the date: {search_date}")


def displayhelp_text():
    global label_warn


    if not label_warn:
        label_warn = tk.Label(
        root,
        text=" To get started, click the dark green button with the text 'Get Weather' to get Temperature (F), and Weather for 15 days and all 24-hour weather and temperature in each day. \nSome data may also change. \n\nData Distinguishing: Hour 00:00 is normally 12:00 AM, but it is the beginning of the next day, so that is why it is at the top. \n\nSearch Bar Help: You can only search for days starting from the current day till 15 days after. \nAdding the hour data will not be used since all hours are just 24 and can easily fit. \n\n\n Click the above button again to close this text."
            )
        label_warn.pack(pady=10)
    else:
        label_warn.destroy()
        label_warn = None


root = tk.Tk()
root.title("Weather Data - Badagry")


weather_data = ""


fetch_button = tk.Button(root, text="Get Weather", command=display_weather, bg="darkgreen", fg="white")
fetch_button.pack(pady=10)


search_frame = tk.Frame(root)
search_frame.pack(pady=10)


search_label = tk.Label(search_frame, text="Search by Date (YYYY-MM-DD):")
search_label.pack(side=tk.LEFT, padx=5)


search_entry = tk.Entry(search_frame, width=15)
search_entry.pack(side=tk.LEFT, padx=5)


search_button = tk.Button(search_frame, text="Search", command=search_by_date, bg="darkblue", fg="white")
search_button.pack(side=tk.LEFT, padx=5)


text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20, state="disabled")
text_area.pack(padx=10, pady=10)


get_directions = tk.Button(root, text="Get Navigation Help", command=displayhelp_text, bg="darkgreen", fg="white")
get_directions.pack(padx=10)


label_warn = None


root.mainloop()
```

## Full backend code:
```
import requests
import pandas as pd
from datetime import datetime


BASE_URL = "https://api.open-meteo.com/v1/forecast"


WEATHER_CODE_MAP = {
    0: "Sunny (Clear sky)",
    1: "Sunny (Mostly clear)",
    2: "Partly cloudy",
    3: "Cloudy sky",
    45: "Foggy weather",
    48: "Less foggy",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Heavy drizzle",
    56: "Freezing Drizzle: Light",
    57: "Freezing Drizzle: Dense",
    61: "Light rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Freezing Rain: Light",
    67: "Freezing Rain: Heavy",
    71: "Light snowfall",
    73: "Moderate snowfall",
    75: "Heavy snowfall",
    77: "Little snow",
    80: "Light rain showers",
    81: "Moderate rain showers",
    82: "Heavy rain showers",
    85: "Snow showers slight",
    86: "Snow showers heavy",
    95: "Mild thunderstorm",
    96: "Thunderstorm with light hail",
    99: "Thunderstorm with heavy hail"
}


def getHourlyWeather():
    try:
        LAT = # Your specified latitude
        LON = # Your specified longitude


        params = {
            "latitude": LAT,
            "longitude": LON,
            "hourly": "temperature_2m,weathercode",
            "timezone": "auto",
            "forecast_days": 15,  
            "past_days": 1,
            "temperature_unit": "fahrenheit"
        }


        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        model = response.json()


        if "hourly" not in model or "temperature_2m" not in model["hourly"] or "weathercode" not in model["hourly"]:
            return "Error: Missing 'hourly' data in the model."


        hourly_forecast = model["hourly"]
        times = hourly_forecast["time"]
        temperatures = hourly_forecast["temperature_2m"]
        weather_codes = hourly_forecast["weathercode"]


        current_date = datetime.now().strftime("%Y-%m-%d")


        today_data = []
        future_data = []
        for i in range(len(times)):
            date, hour = times[i].split("T")
            weather = WEATHER_CODE_MAP.get(weather_codes[i], "Unknown")
            temp = temperatures[i]
            if date == current_date:
                today_data.append([date, hour, weather, f"{temp}°F"])
            else:
                future_data.append([date, hour, weather, f"{temp}°F"])


        today_df = pd.DataFrame(today_data, columns=["Date", "Hour", "Weather", "Temperature"])
        future_df = pd.DataFrame(future_data, columns=["Date", "Hour", "Weather", "Temperature"])


        return "Today\n\n" + today_df.to_string(index=False) + "\n\nNext 15 days\n\n" + future_df.to_string(index=False)
    except Exception as e:
        return f"An error occurred: {e}"
```

Hope you loved this, if so, star ⭐ this repository.
To view this in your computer, using python, run frontend.py, not backend.py.
If you want it online, use the source.html and open it in your browser.

