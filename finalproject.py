import requests  # Importing the requests module
from requests.exceptions import HTTPError

# Intro function contains simple greeting message that welcomes the user to the program


def intro():
    introduction = "\nWelcome to the Python Weather Forecaster\n"
    introduction += "==========================================\n"
    print(introduction)


# Main function below gives the program its core functionality
def main():
    # gather the zipcode from the user
    zipcode = input(
        "Please enter a USA zipcode to recieve the weather forecast: ")
    apiKey = 'c669833723c4189d06973a20b769de00'
    # zipcode input and api key are combined with api endpoint
    url = f'http://api.openweathermap.org/data/2.5/weather?zip={zipcode}&appid={apiKey}&units=imperial'

    # try/except block that validates whether the zipcode input was valid and created a successful connection
    # if input isn't valid, user will recieve an error and be prompted to try again
    try:
        response = requests.get(url)
        response.raise_for_status()
        # parse response to json, and save certain variables in the response to variables so they can later be displayed to the user
        jsonResponse = response.json()
        weatherDescription = jsonResponse['weather'][0]['description']
        weatherTemp = jsonResponse['main']['temp']
        weatherHumidity = jsonResponse['main']['humidity']
        weatherWind = jsonResponse['wind']['speed']
        weatherName = jsonResponse['name']
        # f string combining the variables containing the saved json response in order to display to the user
        msg = f'''The weather forecast for {zipcode} in {weatherName} is: {weatherTemp} Degrees Farenheit, with humidity at {weatherHumidity}%, wind at {weatherWind}mph, and you can expect: {weatherDescription}.'''
        print(msg)
    # Exception logic in the event that the user did not input a valid zipcode or if there was a different error w/ the api connection
    except HTTPError:
        print("....\n")
        print("An HTTP Error Occured. Please ensure you are entering a valid USA zipcode.")
        print("Let's try again.\n.....\n")
        main()  # main function call will restart the program, prompting the user for a valid zipcode
    except Exception:
        print("....\n")
        print(f"An Error Occured. Please ensure you are entering a valid USA zipcode.")
        print("Let's try again.\n.....\n")
        main()

# Again function below employs a while loop giving the user the option to fetch another forecast or quit the application


def again():
    while True:
        continue_status = input(
            "\nRetrieve another forecast? Type 'Y' or 'N': ").upper()
        # Conditional logic that will continue running unless the user enters 'n'
        if continue_status == 'Y':
            main()  # main function call restarts the program in order to fetch another forecast
        elif continue_status == 'N':
            print("\nThank you for using the Python Weather Forecaster. Goodbye!\n")
            break
        else:
            print(
                "\n...\nSorry, you've entered an invalid value. Try again.")


intro()
main()
again()
