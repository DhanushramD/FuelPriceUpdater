
# Fuel Price Updater

## Description ✏
* In our day to day life, we are using our vehicles daily to do our work. 
* And also the fuel price in India is changing everyday. So it is essential to know the latest fuel price. 
* As of now we can only see the fuel price in News websites.
* Using this web app, we can easily know the up-to-date fuel price in all the states in India. 
* Our application fetches the latest fuel price across all the states in India and displays in the app. 
* We developed this in HTML and CSS.
* The UI is user friendly and can be easily understood. 

## Tech Stack

**Client:** Html, CSS

**Server(LocalHost):** Python(Flask, Beautiful Soup)

## Run Locally
To run this Locally you would need python.exe(above version 2) along with pip

Clone the project

```cmd
  git clone https://github.com/Balasuriya29/FuelPriceUpdater.git
```
(or) Download as Zip

Go to the project directory

```cmd
  cd FuelPriceUpdater
```

If you use VS Code

```cmd
  code .
```

Install packages using pip command

```cmd
  pip install flask
  pip install bs4
  pip install requests
  pip install json
```

Start the Server

```cmd
  py app.py
```

Now Ctrl+Click on the Live server in cmd see the web page with current petrol prices. So Every Time we refresh the current value will be updated.
(or)

To get the data in .json format

```cmd
  py fuelpricedata.py
```

Now you can see the generated file named stateWisePrices.json with date on it 

## API Reference

Use the below two api after the localhost address,

ex: http://127.0.0.1:5001/

#### Test API


    GET /

You will see a text - Everything is working fine

#### Get all fuel prices


    GET /petrolprices

To view the webpage



## Screenshots
![Screenshot (124)](https://user-images.githubusercontent.com/100402643/203489260-c1981732-a068-445c-b647-5eb8890ccd00.png)
![Screenshot (125)](https://user-images.githubusercontent.com/100402643/203489272-f2598135-da7f-424f-be3d-39a8e6ae9869.png)



## Demo

[👉Click Here](https://drive.google.com/file/d/1LTq5WF_tuAYQIe3f1CQB-J2Ld9-9Vd6e/view?usp=share_link) - Drive Link of Screen Recording of Our App


## Authors

- [@Balasuriya K A](https://www.github.com/BALASURIYA29)
- [@Renjith Samuel G S](https://www.github.com/renjithsamuel)
- [@Nifaz](https://www.github.com/nifazzz10)
- [@Dhanush Ram D](https://github.com/DhanushramD)

"# FuelPriceUpdater" 
