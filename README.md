# README
### SQLAlch-Currencies-2: 

SQLAlch-Currencies-2 is a Python CLI app that manages crypto currency investments submitted for a bootcamp assignment.

The crypto currency date and rate data is provided with an api from CoinGecko https://www.coingecko.com/ 

This app is based on an awesome Pluralsight coding tutorial by Douglas Starnes who pateiently explains, line by line, how to create the app. https://www.pluralsight.com/.  The tutorial covers using SQLalchemy with a variety of databases, but due to time constraints, this app uses only SQLite. 

The steps below and comments in the files offer instructions for how to use the app. 


### SQLAlch-Currencies-2 Instructions

After cloning the SQLAlch-Currencies-2 repo, cd to the folder, create a venv. 
Install the requests, click and SQLAlchemy packages.

$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install requests SQLAlchemy click

----------------------------------
manager.py contains 4 CLI commands for updating a crypto currency portfolio db
Run this first command to start with a fresh db

$ python manager.py clear-database

Crypto investments are organized into portfolios
Create one or more portfolios to get started

$ python manager.py add-portfolio
Name: Portfolio 1
Description: Description 1

With portfolios created, add individual investments by entering Coin type, Currency purchase and number of coins. (Enter several to see a list of results)

$ python manager.py add-investment
Coin: bitcoin
Currency: USD
Amount: 1.0
1: Portfolio 1
Select a portfolio: 1

$ python manager.py add-investment
Coin: ethereum
Currency: GBP
Amount: 10
1: Portfolio 1
Select a portfolio: 1

Request a portfolio view

$ python manager.py view-portfolio
1: Portfolio 1
Select a portfolio: 1

----------------------------------
The provides instruction for various methods for using code to manage 

----------------------------------
#### main.py
main.py contains CLI commands that update a test SQLite DB using SQL (not ORM)
This helps understand the pros and cons
----------------------------------
#### Bash (not CLI) test instructions: 

demo.py contains examples of bash CRUD commands for updating the test SQLite DB file follow the comments.

Uncomment only the specified code as marked in the demo.py file for each CRUD command, then run python demo.py in the terminal.
You will need to re-comment out the code to view each CRUD method individually
In VSCode, the DB changes can be viewed using the SQLite extention

  - In the VSCode explorer, right click the DB file and select Open Database
  - Expand the resulting lower SQLITE EXPLORER tab
  - Expand the DB name and table name arrows to see the table cols
  - Right click the arrow next to the table name and select "Show Table" to open a view of the table cols and rows

----------------------------------
#### relationships.py 
relationships.py contains  two tables synced with SQLalchemy relationship() function
Follow the comments and view results in the VSCode SQLite explorer tool

----------------------------------




