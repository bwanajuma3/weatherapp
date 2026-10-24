import requests

location = input ("ENTER YOUR CITY: ")
url = "https://api.weatherapi.com/v1/current.json?key=2773c7f6112d40cb99695912262410&q={location}"

response = requests.get(url)
print(response.status_code)

if  response.status_code == 200:
    data = response.json()
    print (data["current"]["temp_c"])
    print (data["current"]["condition"]["text"])
    print (f"In {location} The weather is {data["current"]["condition"]["text"]} and the temperature {data["current"]["temp_c"]} degrees celsius today.")
    


