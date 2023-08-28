# README
### This is for Part 2 - SQLAlch-Currencies-2: 

While the Part 1 (SQLAlch-Currencies) app used SQL statements to populate an SQLite DB for crypto currency investments, this Part 2 app (SQLAlch-Currencies-2) uses the SQLAlchemy ORM and the SQLAlchemy Core API to populate a similar but separate SQLite DB. A comparing the apps helps demonstrate the pros and cons of each method.

The crypto currency date and rate data is provided with an api from CoinGecko https://www.coingecko.com/ 

These apps are based on an awesome Pluralsight tutorial by Douglas Starnes who pateiently explains, line by line, how the apps work. https://www.pluralsight.com/. Pluralsight is awesome and Mr. Starnes is a Tech Rock star.

The steps below outline how to use the app, and comments are provided to hightlight the requirements for this assignment.


### SQLAlch-Currencies-2 Getting Started

After cloning the SQLAlch-Currencies-2 repo, cd to the folder, create a venv. 
Install the requests, click and SQLAlchemy packages.

$ python -m venv venv
$ source venv/bin/activate
(venv) $ python -m pip install requests SQLAlchemy click

Other packages used are already part of the Python Standard Library

----------------------------------
#### CLI instructions: 

CRUD commands for updating the SQLite DB file can be found in the demo.py file comments.
Uncomment only the specified code as marked in the demo.py file for each CRUD command, then run python demo.py in the terminal.
You will need to re-comment out the code to view each CRUD method individually
In VSCode, the DB changes can be viewed using the SQLite extention

  - In the VSCode explorer, right click the DB file and select Open Database
  - Expand the resulting lower SQLITE EXPLORER tab
  - Expand the DB name and table name arrows to see the table cols
  - Right click the arrow next to the table name and select "Show Table" to open a view of the table cols and rows


----------------------------------

The relationshops.py file 


